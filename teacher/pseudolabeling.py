from ultralytics import YOLO
import os,glob,time

def get_image_paths(folder_path):
    # Define the list of image extensions you want to include
    image_extensions = ['*.png', '*.jpg', '*.jpeg', '*.bmp', '*.tiff']
    
    # Initialize an empty list to store image paths
    image_paths = []
    
    # Loop through each extension and get all matching files
    for extension in image_extensions:
        image_paths.extend(glob.glob(os.path.join(folder_path, extension)))
    
    # Convert to absolute paths
    absolute_image_paths = [os.path.abspath(image_path) for image_path in image_paths]
    
    return absolute_image_paths

folder_path = '/data/yechan2468/share/June5th/database' 
album= get_image_paths(folder_path)

    
model = YOLO("/data/yechan2468/share/June5th/best.pt") 

for img in album:
    model.predict(img,save_txt=True,conf=0.8) 
