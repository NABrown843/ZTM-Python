import sys
import os
from PIL import Image, ImageFilter

# grab first and second argument

parent_dir = os.getcwd()
image_folder = os.path.join(parent_dir, sys.argv[1])
output_folder = os.path.join(parent_dir, sys.argv[2])

# check if new exists, if not create

if not os.path.exists(output_folder):
	os.mkdir(output_folder)

# loop through Pokedex, 
# convert images to png,
# save to new folder

for file in os.listdir(image_folder):
	filename = os.path.splitext(file)[0]
	img = Image.open(f'{image_folder}{file}')
	img.save(f'{output_folder}{filename}.png', 'png')