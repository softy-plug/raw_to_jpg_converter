import os
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askdirectory

# Prompt user for folders
Tk().withdraw()
raw_folder = askdirectory(title='Choose the folder with RAW images:')
jpg_folder = askdirectory(title='Choose the folder to save converted JPG images:')

# Check if folders exist, create if they don't
if not os.path.exists(jpg_folder):
    os.makedirs(jpg_folder)

# Loop through all files in RAW folder
for file_name in os.listdir(raw_folder):
    if file_name.endswith('.raw'):
        # Open RAW image and convert to JPG
        raw_file_path = os.path.join(raw_folder, file_name)
        jpg_file_name = os.path.splitext(file_name)[0] + '.jpg'
        jpg_file_path = os.path.join(jpg_folder, jpg_file_name)
        with open(raw_file_path, 'rb') as f:
            raw_data = f.read()
        raw_image = Image.frombytes('RGB', (640, 480), raw_data)

        # Save JPG image with maximum quality
        raw_image.save(jpg_file_path, 'JPEG', quality=100)

print(f"All RAW images in {raw_folder} converted to JPG and saved in {jpg_folder}.")

#softy_plug