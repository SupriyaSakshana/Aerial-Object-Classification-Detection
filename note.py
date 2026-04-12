import gdown

file_id = "1B_UArqFmXjeIKqPGHqt77rUJaHGLigIJ"
output = "/content/dataset.zip"

gdown.download(f"https://drive.google.com/uc?id={file_id}", output, quiet=False)
