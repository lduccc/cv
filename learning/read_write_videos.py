import os 
import cv2
import numpy as np
import matplotlib.pyplot as plt

def video_from_webcam():
    root = os.getcwd()
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()
        if not success:
            break

        cv2.imshow("Webcam", frame)

        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


def video_from_file(input_name):
    root = os.getcwd()
    input_path = os.path.join(root, f"videos\\{input_name}")
    cap = cv2.VideoCapture(input_path)
    
    while True:
        success, frame =  cap.read()
        if not success:
            break

        cv2.imshow("Video", frame)

        if cv2.waitKey(100) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


def write_video_from_webcam(output_name):
    root = os.getcwd()
    cap = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    output_path = os.path.join(root, f"output\\{output_name}")

    out = cv2.VideoWriter(output_path, fourcc, 20.0, (640, 480))

    while True:
        success, frame = cap.read()
        if not success:
            break

        cv2.imshow("Webcam", frame)
        out.write(frame)

        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

def write_video_from_file(input_name, output_name):
    root = os.getcwd()
    input_path = os.path.join(root, f"videos\\{input_name}")
    output_path = os.path.join(root, f"output\\{output_name}")
    cap = cv2.VideoCapture(input_path)
    # fps = cap.get(cv2.GET_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, 60.0, (640, 480))

    while True:
        success, frame = cap.read()
        if not success:
            break
        
        frame = cv2.resize(frame, (640, 480))
        cv2.imshow("Video", frame)
        out.write(frame)

        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

def main():
    # video_from_webcam()
    # video_from_file("sample1.mp4")
    # write_video_from_webcam("webcam_output.avi")
    write_video_from_file("sample1.mp4", "file_output.mp4")

if __name__ == "__main__":
    main()


