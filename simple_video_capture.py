import cv2

cap = cv2.VideoCapture(0)

frame_width, frame_height = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

while True:
    #Read the webcam
    success, frame = cap.read()
    if not success:
        break
    
    #Write frame to output file
    out.write(frame)

    #Show webcam to screen
    cv2.imshow("Camera", frame)

    #End if press "x"
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break


cap.release()
cap.deleteAllWindows()
