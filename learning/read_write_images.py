import cv2, os
import matplotlib.pyplot as plt
import numpy as np


def read_image(name):
    #getcwd is used to get the current working directory
    root = os.getcwd()
    image_path = os.path.join(root, f'images\\{name}')
    print(image_path)
    img = cv2.imread(image_path)

    cv2.imshow("Image", img)
    cv2.waitKey(0)


def write_image(input_name, output_name):
    root = os.getcwd()
    image_path = os.path.join(root, f"images\\{input_name}")
    img = cv2.imread(image_path)

    output_path = os.path.join(root, f"output\\{output_name}")
    cv2.imwrite(output_path, img)
    
def main():
    # read_image("cat2.jpg")
    write_image("cat2.jpg", "cat2_copy.jpg")    

if __name__ == "__main__":
    main()