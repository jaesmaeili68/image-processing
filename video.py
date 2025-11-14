import cv2

video_path = r"E:\Python Tutorial\image processing\video1.MP4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ Error: Could not open video file")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("❌ End of video or cannot read frame")
        break

    if frame is None:
        print("❌ Frame is empty")
        break

    cv2.imshow("Video", frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
#The video will NOT display anything unless cv2.waitKey() is present.
cap.release()
cv2.destroyAllWindows()