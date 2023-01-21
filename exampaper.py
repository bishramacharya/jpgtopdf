import sys
import os
import cv2
from PIL import Image
image_folder = sys.argv[1]
output_folder = sys.argv[2]
image_list=[]
count =1
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    width, height = img.size
    print(img.size)
    left = 0
    top = 200
    right = 1080
    bottom = 2200 
    im1 = img.crop((left, top, right, bottom))
    print("Done !")
    
    image_list.append(im1)
    count +=1
    

im1.save(f'C:/Users/bisra/Desktop/exampaper/{output_folder}/{output_folder}.pdf', save_all=True, append_images=image_list)    