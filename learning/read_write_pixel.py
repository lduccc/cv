import cv2, os
import numpy as np
import matplotlib.pyplot as plt

def read_and_write_pixel_values(input_name):
    root = os.getcwd()
    input_path = os.path.join(root, f"images\\{input_name}")

    img = cv2.imread(input_path)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    imgRGB[280, 100] = [255, 0, 0]  # Set pixel to red
    imgRGB[280, 101] = [0, 255, 0]  # Set pixel to green
    imgRGB[280, 102] = [0, 0, 255]  # Set pixel to blue

    imgRGB[260:340,265:360] = [255, 255, 0]  # Set a block to yellow    
    plt.figure()
    plt.imshow(imgRGB)
    plt.title("Original Image")
    plt.show()


def main():
    read_and_write_pixel_values("cat2.jpg")

if __name__ == "__main__":
    main()