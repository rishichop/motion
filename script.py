import os
import shutil
import pandas as pd


csv_file = 'dataset1/valid/_annotations.csv'  
image_dir = 'dataset1/valid'          
output_dir = 'dataset2/valid'  


df = pd.read_csv(csv_file)



for index, row in df.iterrows():
    img_filename = row['filename']
    class_ = row['class']
    subclass = ""
    if class_ == 0:
        subclass = "sitting"
    else:
        subclass = "standing"
    
    class_folder = os.path.join(output_dir, subclass)

    
    
    src_path = os.path.join(image_dir, img_filename)
    
    
    dest_path = os.path.join(class_folder, img_filename)
    
    
    if os.path.exists(src_path):
        shutil.move(src_path, dest_path)
        print(f"Moved {img_filename} to {class_folder}")
    else:
        print(f"Image {img_filename} not found in {image_dir}")

print("All images have been organized into class folders.")
