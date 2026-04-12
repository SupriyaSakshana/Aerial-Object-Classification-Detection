import gdown

file_id = "1B_UArqFmXjeIKqPGHqt77rUJaHGLigIJ"
output = "/content/dataset.zip"

gdown.download(f"https://drive.google.com/uc?id={file_id}", output, quiet=False)


import zipfile
import os

extract_path = "/content/dataset"

with zipfile.ZipFile(output, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print("Dataset extracted!")
