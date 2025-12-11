import os, cv2
import matplotlib.pyplot as plt
import numpy as np



def median_filtering(input_name):
    root = os.getcwd()
    image_path = os.path.join(root, f"images\\{input_name}")
    image = cv2.imread(image_path)
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    #added noise (based on gaussian idk)
    noisy_image = imageRGB.copy()
    noise_prob = 0.05
    noise = np.random.rand(noisy_image.shape[0], noisy_image.shape[1])
    noisy_image[noise < noise_prob / 2] = 0
    noisy_image[noise > 1 - noise_prob / 2] = 255

    kernel_size = 5
    image_filter = cv2.medianBlur(noisy_image, kernel_size)


    plt.figure()
    plt.subplot(131)
    plt.imshow(imageRGB)
    plt.title("Original image")

    plt.subplot(132)
    plt.imshow(noisy_image)
    plt.title("Noisy image")

    plt.subplot(133)
    plt.imshow(image_filter)
    plt.title("Noisy image after median blur")

    plt.show()
    

def main():
    median_filtering("cat2.jpg")


if __name__ == "__main__":
    main()
