import gdown

# Google Drive file ID and output path
file_id = '1mcIJA3Ddgb_G2rLsD7lPe-MFPwceZSvj'
output = 'saved_model/model.safetensors'

# Download the file
gdown.download(f"https://drive.google.com/uc?id={file_id}", output, quiet=False)