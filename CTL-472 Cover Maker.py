#Wacom CTL 472

from PIL import Image
import requests
import os

requestHeaders = {"User-Agent": "CTL 472 Cover Maker"}
img_size = (1050, 730)

def KillProgram(): os.system(f"taskkill /f /pid {os.getpid()}")

try: print("\nex) https://redstar.moe/b/1919312 --> BeatmapID = 1919312"); bid = int(input("Input BeatmapID : "))
except Exception as e: print(f"\n{e}\n"); input("ERROR! TRY AGAIN"); KillProgram()

with open("CTL472.jpg", "wb") as f:
    r = requests.get(f"https://b.redstar.moe/bg/{bid}", headers=requestHeaders)
    if r.status_code == 200: f.write(r.content)
    else: input("ERROR!"); KillProgram()

#with Image.open("lol.jpg") as img:
with Image.open("CTL472.jpg") as img:
    img = img.convert("RGB")
    width, height = img.size
    if width / height > 4 / 3:
        croped_width = height * (4 / 3) #원본기준 4:3 비율 (width)
        left = (width - croped_width) / 2
        top = 0
        right = width - left
        bottom = height
    else:
        croped_height = width / (4 / 3) #원본기준 4:3 비율 (height)
        left = 0
        top = (height - croped_height) / 2 # = 160.5
        right = width
        bottom = height - top

    img_cropped = img.crop((left,top,right,bottom))
    img_cropped.resize(img_size, Image.LANCZOS).save("CTL472-1050x730.jpg", quality=100)

os.remove("CTL472.jpg")

input("\nCTL472-1050x730.jpg \nDone\nexit this program")
