import os, cv2
import matplotlib.pyplot as plt
import numpy as np

def image_resize(input_name):
    root = os.getcwd()
    image_path = os.path.join(root, f"images\\{input_name}")
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    sub_image = image[220:380, 250:380, :] #eye
    height, width, _ = sub_image.shape

    interpolation_methods = {
        "Area": cv2.INTER_AREA,
        "Linear": cv2.INTER_LINEAR,
        "Nearest": cv2.INTER_NEAREST,
        "Cubic": cv2.INTER_CUBIC,
        "Lanczos4": cv2.INTER_LANCZOS4,
    }

    plt.figure()
    plt.subplot(2, 3, 1)
    plt.imshow(sub_image)
    plt.title("Original Image")
 
    
    scale = 5 #scale for resizing

    for i, (name, method) in enumerate(interpolation_methods.items()):
        plt.subplot(2, 3, i + 2)
        image_resize = cv2.resize(sub_image, (int(width * scale), int(height * scale)), method)
        plt.imshow(image_resize)
        plt.title(name)

    plt.show() 
    # image_ = image[:,:,2]
    # zeros = np.zeros_like(image_)

    # plt.figure()
    # plt.subplot(131)
    # plt.imshow(cv2.merge([image[:,:,0], zeros, zeros]))
    # plt.subplot(132)
    # plt.imshow(cv2.merge([zeros, image[:,:,1], zeros]))
    # plt.subplot(133)
    # plt.imshow(cv2.merge([zeros, zeros, image[:,:,2]]))    

def main():
    image_resize("cat2.jpg")

if __name__ == "__main__":
    main()