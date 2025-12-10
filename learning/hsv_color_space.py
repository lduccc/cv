import os, cv2
import numpy as np
import matplotlib.pyplot as plt


def hsv_value_computute(r, g, b):
    cmax = np.maximum(np.maximum(r, g), b)
    cmin = np.minimum(np.minimum(r, g), b)

    delta = cmax - cmin

    hue = np.zeros_like(cmax)

    mask_delta = delta > 0 #remove division by zero
    mask_r = (cmax == r) & mask_delta
    mask_g = (cmax != r) & (cmax == g) & mask_delta
    mask_b = (cmax != r) & (cmax != g) & (cmax == b) & mask_delta

    hue[mask_r] = (60 * ((g[mask_r] - b[mask_r]) / delta[mask_r]) + 360) % 360
    hue[mask_g] = (60 * ((b[mask_g] - r[mask_g]) / delta[mask_g]) + 120) % 360
    hue[mask_b] = (60 * ((r[mask_b] - g[mask_b]) / delta[mask_b]) + 240) % 360 

    saturation = np.zeros_like(cmax)
    mask_cmax = cmax > 0

    saturation[mask_cmax] = delta[mask_cmax] / cmax[mask_cmax] * 100

    value = cmax * 100
    # if cmax == cmin:
    #     hue = 0
    # elif cmax == r:
    #     hue = (60 * ((g - b) / delta) + 360) % 360
    # elif cmax == g:
    #     hue = (60 * ((b - r) / delta) + 120) % 360
    # else:
    #     hue = (60 * ((r - g) / delta) + 240) % 360

    # if cmax == 0:
    #     saturation = 0
    # else:
    #     saturation = delta / cmax * 100

    # value = cmax * 100

    return hue, saturation, value

def rgb_to_hsv_formula(image_name):
    root = os.getcwd()
    input_path = os.path.join(root, f"images\\{image_name}")

    image = cv2.imread(input_path)
    b,g,r = cv2.split(image.astype("float32") / 255.0)


    hue, saturation, value = hsv_value_computute(r, g, b)
    hsv_image = cv2.merge([hue / 2, saturation * 2.55, value * 2.55]).astype(np.uint8)

    hsv_original = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    cv2.imshow("HSV Image", cv2.cvtColor(hsv_image,cv2.COLOR_HSV2BGR))
    # cv2.imshow("OpenCV", hsv_original)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    rgb_to_hsv_formula("cat2.jpg")

if __name__ == "__main__":
    main()