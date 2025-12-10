import os, cv2
import matplotlib.pyplot as plt
import numpy as np


def convolution_2d(input_name):
    #blur images using kernel
    root = os.getcwd()
    input_path = os.path.join(root, f"images\\{input_name}")
    image = cv2.imread(input_path)
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    kernel_sizes = [3, 5, 10, 20, 50]

    plt.figure()
    plt.subplot(2, 3, 1)

    plt.imshow(imageRGB)
    plt.title("Original Image")

    for i, kernel_size in enumerate(kernel_sizes):
        kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size ** 2)
        image_filter = cv2.filter2D(imageRGB, -1, kernel)

        plt.subplot(2, 3, i + 2)
        plt.imshow(image_filter)

        plt.title(f"Kernel size: {kernel_size}x{kernel_size}")

    plt.show()


def main():
    convolution_2d("cat2.jpg")

if __name__ == "__main__":
    main()