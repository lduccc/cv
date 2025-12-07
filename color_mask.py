import cv2
import numpy as np

cap = cv2.VideoCapture(0)


def get_hsv_limits(bgr_color, h_pad = 10, sv_pad = 50):
    #return lower and upper limit for bgrcolors -> hsv colors
    hsv_color = cv2.cvtColor(bgr_color, cv2.COLOR_BGR2HSV)
    h, s, v = hsv_color[0][0][0], hsv_color[0][0][1], hsv_color[0][0][2]

    lower_limit = np.array([
        np.clip(h - h_pad, 0, 179),
        np.clip(s - sv_pad, 0, 255),
        np.clip(v - sv_pad, 0, 255)
    ], dtype = np.uint8)

    upper_limit = np.array([
        np.clip(h + h_pad, 0, 179),
        np.clip(s + sv_pad, 0, 255),
        np.clip(v + sv_pad, 0, 255)
    ], dtype = np.uint8)

    return lower_limit, upper_limit
#Range of blue color in HSV
#remember OpenCV uses BGR format instead of RGB

color = np.uint8([[[121, 154, 196]]]) ## skin 
padding_hue, padding_rest = 10, 50
hsvColor = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
kernel_blur = (5, 5)
kernel_moprh = np.ones((3,3), np.uint8)
#set lower and upper hsv bounds
lower_limit, upper_limit = get_hsv_limits(color, padding_hue, padding_rest)

while True:
    success, frame = cap.read()

    if not success:
        break

    #pre_processing to smooth (blur) the image 
    blurred_frame = cv2.GaussianBlur(frame, kernel_blur, 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    #inrange -> returns white mask if pixel is between lower_limit and upper_limit, else black
    mask = cv2.inRange(hsv, lower_limit, upper_limit)

    #post_processing
    #erosion -> shrinks, thins the boundaries of objects + removing lonely pixel islands on edges
    #dilation -> expands the boundaries -> making objects bigger + fill in small gaps and holes
    mask = cv2.erode(mask, kernel_moprh)
    mask = cv2.dilate(mask, kernel_moprh)

    #filter mask in frame
    result = cv2.bitwise_or(frame, frame, mask = mask) #? 

    mask_3ch = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    display = np.hstack([mask_3ch, result])

    cv2.imshow("mask", mask)
    cv2.imshow("webcam", frame)
    cv2.imshow("blurred", blurred_frame)
    cv2.imshow("hehehe", result)
    cv2.imshow("hehehe", display)


    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()