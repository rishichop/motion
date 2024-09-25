import os
import shutil
import pandas as pd

# Paths
csv_file = 'dataset1/valid/_annotations.csv'  # Path to your CSV file
image_dir = 'dataset1/valid'          # Directory where all images are stored initially
output_dir = 'dataset2/valid'  # Output directory where images will be organized

# Read the CSV file
df = pd.read_csv(csv_file)


# Iterate through each row in the CSV file
for index, row in df.iterrows():
    img_filename = row['filename']
    class_ = row['class']
    subclass = ""
    if class_ == 0:
        subclass = "sitting"
    else:
        subclass = "standing"
    # Create a class folder if it doesn't exist
    class_folder = os.path.join(output_dir, subclass)

    
    # Source image path
    src_path = os.path.join(image_dir, img_filename)
    
    # Destination image path
    dest_path = os.path.join(class_folder, img_filename)
    
    # Move the image to the class folder
    if os.path.exists(src_path):
        shutil.move(src_path, dest_path)
        print(f"Moved {img_filename} to {class_folder}")
    else:
        print(f"Image {img_filename} not found in {image_dir}")

print("All images have been organized into class folders.")
