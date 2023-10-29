import sys
from PIL import Image

def main():
    images = [] # An empty list for storing images
    
    # Loop through the command-line args for the images (Max 3)
    # Append each image to the list 
    if not len(sys.argv[1:]) == 4:
        sys.exit("\n3 images and a speed\n")
    elif not sys.argv[4].isdigit():
        sys.exit("\nFourth argument must be a number\n")
    else:
        for arg in sys.argv[1:-1]:
            image = Image.open(arg)
            images.append(image)

        save_gif(images, sys.argv[4])

def save_gif(images, speed_num):
    # Save the images as a gif with the disired speed.
    speed = int(speed_num)
    images[0].save(
    "My_Gif.gif", save_all = True, 
    append_images=[images[1], images[2]], 
    duration=speed, loop=0
    )

def is_float(num):
    try:
        return float(num)
    except ValueError:
        return False

if __name__ == '__main__':
    main()
