import cv2
import time
import numpy as np
from PIL import ImageGrab

width = 1920
height = 1080
time_stamp = time.strftime('%Y-%m-%d %H-%M-%S')
file_name = f"screen_recodes/record {time_stamp}.mp4"
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(file_name, fourcc, 60.0, (width, height))

while True:
    img = ImageGrab.grab((0, 0, 1920, 1080))
    img_final = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    cv2.imshow('Secret Capture', img_final)
    captured_video.write(img_final)
    if cv2.waitKey(1) == ord('q'):
        break
