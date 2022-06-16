import os
import re
from PIL import Image

folder = input('Path to files folder: ')
folder = folder.replace('"', '')
if folder[-1] != '\\':
    folder = folder + '\\'


files = os.listdir(folder)
files.sort(key=lambda f: int(re.sub('\D', '', f)))
pdf_path = input('File name: ') + '.pdf'



for i in files:
    print(i)

image_files = []
for i in range(1, len(files)):
    image_files.append(Image.open(folder + files[i]))

cover = Image.open(folder + files[0])

cover.save(pdf_path, resolution=50.0, save_all=True, append_images=image_files)
print('DONE')