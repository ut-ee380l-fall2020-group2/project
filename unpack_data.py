import sys
import os
import zipfile

data_dir = sys.argv[1]
zips = sys.argv[2:]

if not os.path.exists(data_dir):
    os.mkdir(data_dir)
    
for _zip in zips:
    with zipfile.ZipFile(_zip, 'r') as zip_ref:
        zip_ref.extractall(data_dir)