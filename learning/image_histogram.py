import os, cv2
import matplotlib.pyplot as plt
import numpy as np

def gray_histogram(input_name):
    root = os.getcwd()
    input_path = os.path.join(root, f"images\\{input_name}")
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    plt.figure()
    plt.imshow(image, cmap = "gray")

    hist = cv2.calcHist([image], [0], None, [256], [0,256])
    plt.figure()
    plt.plot(hist)
    plt.xlabel("Pixel value")
    plt.ylabel("Number of pixels")


    plt.show()

def color_histogram(input_name):
    root = os.getcwd()
    input_path = os.path.join(root, f"images\\{input_name}")
    image = cv2.imread(input_path)
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    colors = ("r", "g", "b")
    plt.figure()
    plt.imshow(imageRGB)
    plt.figure()

    for i, color in enumerate(colors):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color = color)
        plt.xlabel("Pixel value")
        plt.ylabel("Number of pixels")

    plt.show()

def main():
    # gray_histogram("cat2.jpg")
    color_histogram("cat2.jpg")

if __name__ == "__main__":
    main()