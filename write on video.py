import cv2
import numpy as np

video_path = r"E:\Python Tutorial\image processing\video1.MP4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ Error: Could not open video file")
    exit()

while True:
    ret, frame = cap.read()
    cv2.line(frame, (200, 200), (100, 100), (255, 0, 0), 10, lineType= 12)
    cv2.rectangle(frame, (200, 200), (100, 100), (0, 255, 0), 10)
    cv2.circle(frame, (200, 200), 100, (0, 255, 0), 10)

    pts = np.array([[10, 20], [50, 200], [200, 100], [200, 20]])
    cv2.polylines(frame, [pts], True, (150, 0, 0), 5)

    text = "amoo"
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame, text, (100, 100), font, 3, (100, 50, 0), 20)


    if not ret:
        print("❌ End of video or cannot read frame")
        break

    if frame is None:
        print("❌ Frame is empty")
        break

    cv2.imshow("Video", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
#The video will NOT display anything unless cv2.waitKey() is present.
cap.release()
cv2.destroyAllWindows()