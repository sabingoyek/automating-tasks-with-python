import os
from PIL import Image

directory = 'images'
dest_path = "./opt/icons"

for filename in os.listdir(directory):
    #print(filename)
    path = os.path.join(directory, filename)
    save_path = os.path.join(dest_path, filename+".jpg")
    #print(save_path)
    img = Image.open(path)
    new_img = img.rotate(-90).resize((128,128)).convert("RGB")
    #new_img.save(filename+".jpg")
    new_img.save(save_path)