import cv2
import sys

if not os.path.exists('frames'):
    os.mkdir('frames')

cap = cv2.VideoCapture(PATH_TO_VIDEO)

# https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-get
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html

frame_index = 0
while cap.isOpened():
    success, frame = cap.read()

    if not success:
        print("an error occured at ", frame_index)
        break

    cv2.imwrite('./frames/'+str(frame_index)+'.jpg', frame, )

    frame_index += 1

cap.release()
cv2.destroyAllWindows()

print("done")