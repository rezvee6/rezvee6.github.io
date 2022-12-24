import os
from PIL import Image

# Get the current directory
directory = os.getcwd()

# Set the desired width and height
width = 3840
height = 2160

# Iterate over all files in the directory
for filename in os.listdir(directory):
  # Check if the file is an image
  if filename.endswith('.jpg') or filename.endswith('.png'):
    # Open the image
    image = Image.open(os.path.join(directory, filename))
    # Resize the image
    image = image.resize((width, height), Image.ANTIALIAS)
    # Save the resized image
    image.save(os.path.join(directory, filename))