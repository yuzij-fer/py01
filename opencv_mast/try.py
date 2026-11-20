from ultralytics import YOLO
import cv2

model = YOLO('best.pt')
cap = cv2.VideoCapture('ms.mp4')
while True:
    ret, frame = cap.read()
    if not ret: break
    results = model(frame,conf=0.3, verbose=False)
    annotated_frame = results[0].plot()
    cv2.imshow("RM Armor Detect", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()