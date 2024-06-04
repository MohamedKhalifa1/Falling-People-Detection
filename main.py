import cv2
from ultralytics import YOLO

model = YOLO('C:/Users/lab11/PycharmProjects/pythonProject5/yolo_weights/yolov8_fall_detection.pt')
results = model("C:/Users/lab11/PycharmProjects/pythonProject5/images/all_about_people_cover.jpeg", show=True)
cv2.waitKey(0)