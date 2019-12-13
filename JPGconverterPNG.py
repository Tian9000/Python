import sys
import os
from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
ouput_folder = sys.argv[2]

if not os.path.exists(ouput_folder):
    os.makedirs(ouput_folder)
    
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    
    img.save(f'{ouput_folder}{clean_name}.png', 'png')
    print('all done')
