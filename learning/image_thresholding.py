import os, cv2
import matplotlib.pyplot as plt
import numpy as np

def thresholding(input_name):
    root = os.getcwd()
    input_path = os.path.join(root, "images", input_name)
    image = cv2.imread(input_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    hist = cv2.calcHist([image_gray], [0], None, [256], [0, 256])
    plt.figure()
    plt.subplot(241)
    plt.imshow(image_rgb)
    plt.title("Original image")
    
    plt.subplot(242)
    plt.imshow(image_gray, cmap = "gray")
    plt.title("Grayscale image")

    plt.subplot(243)
    plt.plot(hist)
    plt.xlabel('Pixel intensity')
    plt.ylabel('Number of pixels')


    threshold_options = {
        "Binary" : cv2.THRESH_BINARY,
        "Binary Inverse" : cv2.THRESH_BINARY_INV,
        "To Zero" : cv2.THRESH_TOZERO,
        "To Zero Inverse" : cv2.THRESH_TOZERO_INV,
        "Trunc" : cv2.THRESH_TRUNC
    }

    thres = 70

    for i, (threshold_name, threshold_opt) in enumerate(threshold_options.items()):
        plt.subplot(2, 4, i + 4)
        _, dst = cv2.threshold(image, thres, 255, threshold_opt)
        plt.imshow(dst, cmap = 'gray')
        plt.title(threshold_name)
    plt.show()


def main():
    thresholding("rose.jpg")

if __name__ == "__main__":
    main()
