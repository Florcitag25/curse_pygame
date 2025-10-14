from PIL import Image,ImageOps
import glob

path = "character/FA_TEDDY_Walk_000.png"

frames = [ImageOps.mirror(Image.open(img).convert("RGBA")) for img in (glob.glob("character\*.png"))]

frames[0].save("character.gif",
                save_all=True,
                append_images=frames[1:],
                duration=50,
                loop=0, 
                disposal=2, 
                transparency=0)