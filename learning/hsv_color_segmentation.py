import os, cv2
import numpy as np
import matplotlib.pyplot as plt


def color_segmentation(image_name):
    root = os.getcwd()
    input_path = os.path.join(root, f"images\\{image_name}")
    image = cv2.imread(input_path)
    image = cv2.GaussianBlur(image, (7, 7), 0)
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_hsv = np.array([0, 0, 0])
    upper_hsv = np.array([30, 180, 120])

    mask = cv2.inRange(imageHSV, lower_hsv, upper_hsv)
    mask_inverse = cv2.bitwise_not(mask)
    extracted = cv2.bitwise_and(imageRGB, imageRGB, mask = mask)
    extracted2 =  cv2.bitwise_and(imageRGB, imageRGB, mask = mask_inverse)
    # image
    plt.figure()
    plt.subplot(221)
    plt.imshow(imageRGB)
    plt.title("cat")

    plt.subplot(222)
    plt.imshow(mask)
    plt.title("mask")

    plt.subplot(223)
    plt.imshow(extracted)
    plt.title("final")

    plt.subplot(224)
    plt.imshow(extracted2)
    plt.title("final")
    plt.show()

def main():
    color_segmentation("cat2.jpg")

if __name__ == "__main__":
    main()