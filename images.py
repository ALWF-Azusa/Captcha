import cv2
import numpy as np
import os

path = "./raw-img/sheep/work"
dirs = os.listdir(path)

def mark_pixels_as_white(rgb_image_path, binarized_image_path, count):
    # Load the RGB image
    rgb_image = cv2.imread(rgb_image_path)

    # Check if the image was loaded successfully
    if rgb_image is None:
        print(f"Error loading image: {rgb_image_path}")
        return

    # Get dimensions of the RGB image
    rgb_height, rgb_width,_ = rgb_image.shape


    # Load the binarized image
    binarized_image = cv2.imread(binarized_image_path, cv2.IMREAD_GRAYSCALE)

    # Resize the binarized image to match the dimensions of the RGB image
    binarized_image = cv2.resize(binarized_image, (rgb_width, rgb_height))

    # Create a mask where white pixels in the binarized image are True
    mask = binarized_image == 255

    # Set white pixels in the RGB image to white
    rgb_image[mask] = [255, 255, 255]  # Set white color (BGR value)

    # Display or save the resulting image
    cv2.imshow('Result', rgb_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('./ans/{}.png'.format(str(count)), rgb_image)

# Example usage
for i in dirs:
    rgb_image_path = './raw-img/sheep/work/{}'.format(str(i))  # Modify the path
    binarized_image_path = 'circular_noise_captcha.png'  # Make sure this is the correct path
    mark_pixels_as_white(rgb_image_path, binarized_image_path, i)

    

    