import os
import re
from pathlib import Path

folder = input('Path to files folder: ')
folder = folder.replace('"', '')
if folder[-1] != '\\':
    folder = folder + '\\'


files = os.listdir(folder)
files.sort(key=lambda f: int(re.sub('\D', '', f)))


for i in files:
    source = folder + i
    
    target = source + '.jpg'

    os.rename(source, target)


print('Done')
