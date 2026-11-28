"""safezone.py - draw the vertical-video safe zones over frames of a reel, to check text and eye line before delivery.
Zones measured off omgadrian's reel DdOy0cnI10R (2026-09-13), on a 1080x1920 frame:
  green  y 0..620        hook text goes here, big
  line   y 625           eye line (upper third)
  blue   y 1293..1572    subtitles go here
  red    y 1572..1920    covered by username and caption
  red    x 855..1080 from y 640 down   covered by like, comment, share
usage: python -I tools/safezone.py <video> <out.jpg> t1 [t2 ...]"""
import subprocess, sys, os, tempfile
from PIL import Image, ImageDraw
HOOK = (0, 0, 1080, 620); EYE = 625; SUB = (0, 1293, 855, 1572); BOT = (0, 1572, 1080, 1920); SIDE = (855, 640, 1080, 1572)
def mark(im):
    im = im.convert("RGBA").resize((1080, 1920)); ov = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    d.rectangle(HOOK, fill=(0, 200, 0, 45)); d.rectangle(SUB, fill=(0, 120, 255, 50))
    d.rectangle(BOT, fill=(220, 0, 0, 90)); d.rectangle(SIDE, fill=(220, 0, 0, 90))
    d.line((0, EYE, 1080, EYE), fill=(0, 255, 0, 255), width=5)
    for x in (360, 720): d.line((x, 0, x, 1920), fill=(255, 255, 255, 120), width=2)
    for y in (640, 1280): d.line((0, y, 1080, y), fill=(255, 255, 255, 120), width=2)
    return Image.alpha_composite(im, ov).convert("RGB")
if __name__ == "__main__":
    video, out, times = sys.argv[1], sys.argv[2], sys.argv[3:]
    tiles = []
    for t in times:
        p = os.path.join(tempfile.gettempdir(), "sz-%s.png" % t.replace(".", "_"))
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", t, "-i", video, "-frames:v", "1", p], check=True)
        tiles.append(mark(Image.open(p)).resize((540, 960)))
    sheet = Image.new("RGB", (540 * len(tiles), 960))
    for i, t in enumerate(tiles): sheet.paste(t, (540 * i, 0))
    sheet.save(out, quality=88); print(out)
