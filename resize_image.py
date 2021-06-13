import os
import sys
import time
from PIL import Image

# Make a folder name as 'Input_Folder'
# Store all image in 'Input_Folder'
# Change `source_path` with 'Input_Folder' location

source_path = r'C://Users/shubh/Desktop/'+'Input_Folder/'

# Create 'Output_Folder' path
destination_path = source_path.replace("Input_Folder", "Output_Folder")

len(os.listdir(source_path))

if os.path.exists(source_path):
    i = 0
    # Make 'Output_Folder' if not exists
    if os.path.exists(destination_path) == False:
        os.makedirs(destination_path)

    # Image Resize
    for file in os.listdir(source_path):
        source_image = source_path+"/"+file
        image = Image.open(source_image)

        # Rename 'Output_Folder' image with 0,1,2,3...
        # If you didn't Rename 'Output_Folder' image then remove # from the below line of code and add # with the next two lines of code
        # destination_image = destination_path+"/"+file
        image_name_and_extension = os.path.splitext(file)
        destination_image = destination_path+"/"+str(i)+image_name_and_extension[1] 

        # You can change Image dimensions with `resize((hight,width))`
        image = image.resize((640,360))
        image.save(destination_image)
        i=i+1
else: print("Please check source_path")