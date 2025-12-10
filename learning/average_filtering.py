import os, cv2
import matplotlib.pyplot as plt
import numpy as np


def on_trackbar_change(value):
    print(f"Kernel size changed to: {value}")

def avg_filtering(input_name):
    root = os.getcwd()
    input_path = os.path.join(root, f"images\\{input_name}")
    image = cv2.imread(input_path)


    cv2.namedWindow("win", cv2.WINDOW_NORMAL)
    cv2.createTrackbar("kernel_size_trackbar", "win", 1, 100, on_trackbar_change)

    height, width, _ = image.shape
    scale = 1

    image_resize = cv2.resize(image, (int(width * scale), int(height * scale)))
    
    while True:
        if cv2.waitKey(1) == ord("q"):
            break

        kernel_size = cv2.getTrackbarPos("kernel_size_trackbar", "win")
        if kernel_size == 0:
            continue
        image_filter = cv2.blur(image_resize, (kernel_size, kernel_size))

        cv2.imshow("win", image_filter)

    
    cv2.destroyAllWindows()


def main():
    avg_filtering("cat2.jpg")

if __name__ == "__main__":
    main()