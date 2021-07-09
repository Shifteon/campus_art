from PIL import Image
import os, sys

resize_method = Image.ANTIALIAS
max_width = 320
max_height = 500
extensions = ['JPG']

read_path = os.path.join(sys.path[0], "media/pictures")
write_path = os.path.join(sys.path[0], "media/small_pictures")

# Function takes in width, height of image and returns the new size.
def adjust_size(width, height):
    if width > max_width:
        if width > height:
            return max_width, int (max_width * height/ width)
        else:
            return int (max_height*width/height), max_height
    else:
        return width, height

# Loads each image from the pictures folder and saves it in the new size in the small_pictures folder.
if __name__ == '__main__':
    for f in os.listdir(read_path):
        if os.path.isfile(os.path.join(read_path, f)):
            f_text, f_ext = os.path.splitext(f)

        print("file name: " + f_text + f_ext)

        image = Image.open(os.path.join(read_path, f))
        width, height = image.size
        image = image.resize(adjust_size(width, height))

        image.save(os.path.join(write_path, f))
        print("Image saved at " + write_path + "/" + f)
    
    print("Image Scaling Completed.")