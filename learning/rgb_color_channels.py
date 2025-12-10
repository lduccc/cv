import cv2, os
import matplotlib.pyplot as plt
import numpy as np

def pureColors():
    zeros = np.zeros((100, 100))
    ones = np.ones((100, 100)) 

    blue = cv2.merge([zeros, zeros, ones * 255])
    red = cv2.merge([ones * 255, zeros, zeros])
    green = cv2.merge([zeros, ones * 255, zeros])

    black = cv2.merge([zeros, zeros, zeros])
    white = cv2.merge([ones * 255, ones * 255, ones * 255])
    yellow = cv2.merge([ones * 255 , ones * 255, zeros]) 

    plt.figure()
    plt.subplot(231)
    plt.title("Red")
    plt.imshow(red)

    plt.subplot(232)
    plt.title("Green")
    plt.imshow(green)
    
    plt.subplot(233)
    plt.title("Blue")
    plt.imshow(blue)
   
    plt.subplot(234)
    plt.title("Black")
    plt.imshow(black)
    
    plt.subplot(235)
    plt.title("White")
    plt.imshow(white)

    plt.subplot(236)
    plt.title("Yellow")
    plt.imshow(yellow)
    plt.show()


def extract_color_channels(image_name):
    
    root = os.getcwd()
    input_path = os.path.join(root, f"images\\{image_name}")

    image = cv2.imread(input_path)
    m,n,_ = image.shape

    b,g,r = cv2.split(image)
    zeros = np.zeros((m,n), dtype="uint8")

    blue = cv2.merge((b, zeros, zeros))
    red = cv2.merge((zeros, zeros, r))
    green = cv2.merge((zeros, g, zeros))

    plt.figure()
    plt.subplot(131)
    plt.title("red")
    plt.imshow(red)

    plt.subplot(132)
    plt.title("green")
    plt.imshow(green)

    plt.subplot(133)
    plt.title("blue")
    plt.imshow(blue)

    plt.show()
def main():
    # pureColors()
    extract_color_channels("cat2.jpg")

if __name__ == "__main__":
    main()