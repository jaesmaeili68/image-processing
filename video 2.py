import cv2

video_path = r"E:\Python Tutorial\image processing\video1.MP4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("the video does not exist")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("end of video")
        break
    if frame is None:
        print("frame is empty")
        break

    cv2.imshow("video", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
