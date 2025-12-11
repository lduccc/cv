import os, cv2
import numpy as np
import matplotlib.pyplot as plt

def gaussian_kernel(ksize, sigma):
    kernel_1d = cv2.getGaussianKernel(ksize, sigma)
    kernel_2d = np.outer(kernel_1d, kernel_1d)

    return kernel_2d

def gaussian_filtering(input_name):
    root = os.getcwd()
    input_path = os.path.join(root, "images", input_name)

    image = cv2.imread(input_path)
    # image_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    ksize, sigma = 101, 20
    kernel = gaussian_kernel(ksize, sigma)

    #3d gaussian meshgrid

    fig = plt.figure()
    # plt.subplot(121)
    # plt.imshow(image_RGB)
    # plt.title("Original image")

    # plt.subplot(121)
    # plt.imshow(kernel)
    # plt.title("Kernel")

    # sub1 = fig.add_subplot(122, projection = '3d')
    # x = np.arange(0, ksize, 1)
    # y = np.arange(0, ksize, 1)

    # xx, yy = np.meshgrid(x, y)

    # sub1.plot_surface(xx, yy, kernel, cmap = 'viridis')
    # plt.show()

    win = "Gaussian Filter"
    cv2.namedWindow(win)
    cv2.createTrackbar('sigma', win, 1, 20, on_trackbar_change_sigma)

    height, width, _ = image.shape
    scale = 1
    image_resize = cv2.resize(image, (int(width * scale), int(height * scale)))

    while True:
        if cv2.waitKey(1) == ord("q"):
            break

        sigma = cv2.getTrackbarPos('sigma', win)
        image_filter = cv2.GaussianBlur(image_resize, (ksize, ksize), sigma)

        cv2.imshow(win, image_filter)

    cv2.destroyAllWindows()

def on_trackbar_change_sigma(value):
    print(f"Sigma value changed to: {value}")

def main():
    gaussian_filtering("cat2.jpg")

if __name__ == "__main__":
    main()