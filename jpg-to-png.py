'''
write a py script which accepts two arguments: 
first: a folder which contains jpg images  
second: name of the new folder where the images will be saved in png format. if it does not exist, create it

eg. the command would look like this:
python jpg-to-png.py images/ new/
^arg [0]      ^arg[1] ^arg[2] 

'''

import sys
import os
from PIL import Image

#grab the arguments
image_folder = sys.argv[1]
output_folder = sys.argv[2]
print (image_folder, output_folder)

#check if 'output_folder' exists; if not, create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder) #makes a new folder
    
#loop thru all the files in the 'image_folder' and convert them to png
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0] #separates the name and extension 
    print(clean_name)
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('conversion complete!')
