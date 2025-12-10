import os, cv2
import matplotlib.pyplot as plt
import numpy as np

def grayscale_image_with_formula(input_name):
    root = os.getcwd()
    input_path = os.path.join(root, f"images\\{input_name}")
    image = cv2.imread(input_path)

    b,g,r = cv2.split(image)
    grayscale = 0.299 * r + 0.587 * g + 0.114 * b

    grayscale_img = cv2.merge([grayscale] * 3)
    # print(grayscale_img.dtype)
    cv2.imshow("Grayscale Image", grayscale_img.astype(np.uint8))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    plt.title("grayscale Image")
    plt.imshow(grayscale_img.astype(np.uint8))
    plt.show()
    
def grayscale_image(input_name):
    root = os.getcwd()
    input_path = os.path.join(root, f"images\\{input_name}")
    image = cv2.imread(input_path)

    imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", imgGray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def read_image_grayscale(input_name):
    root = os.getcwd()
    input_path = os.path.join(root, f"images\\{input_name}")

    #IMREAD_GRAYSCALE is used to directly read the image in grayscale mode
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    cv2.imshow("Grayscale Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    # grayscale_image_with_formula("cat2.jpg")
    # grayscale_image("cat2.jpg")
    read_image_grayscale("cat2.jpg")

if __name__ == "__main__":
    main()