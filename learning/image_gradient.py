import os, cv2
import matplotlib.pyplot as plt
import numpy as np

def image_gradient(input_name):
    root = os.getcwd()
    input_path = os.path.join(root, "images", input_name)

    image = cv2.imread(input_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    kernel_size = 25

    plt.figure()
    plt.subplot(221)
    plt.imshow(image_gray, cmap = "gray")

    plt.subplot(222)
    laplacian_image = cv2.Laplacian(image_gray, cv2.CV_64F, ksize = kernel_size)
    plt.imshow(laplacian_image, cmap = "gray")

    kx, ky = cv2.getDerivKernels(1, 0, 3)
    print(ky@kx.T)

    
    plt.subplot(223)



    plt.show()

def main():
    image_gradient("cat2.jpg")

if __name__ == "__main__":
    main()