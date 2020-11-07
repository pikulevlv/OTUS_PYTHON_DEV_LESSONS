import cv2
FRONTAL_FACE = "haarcascade_frontalface_default.xml"
# создаем БД
faces_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + FRONTAL_FACE)

# print(img.shape)
# print(img.ndim)

def main(cap):

    frame_count = 0
    faces = []

    while True:
        success, img = cap.read()
        if not success:
            print("Couldnt read frame")
            break

        if frame_count % 5 == 0: # обновляем фейся 1 раз в 5 итераций
            faces = faces_cascade_db.detectMultiScale(img)
        frame_count += 1

        for i, (x, y, w, h) in enumerate(faces, start=1):
            pt1 = (x, y)  # upper left
            pt2 = (x + w, y + h)  # lower right
            B = (i * 10 + int(x) * i) % 255
            G = (i * 25 + int(y) * i) % 255
            color = (B, G, 255)
            thickness = 2
            cv2.rectangle(img, pt1, pt2, color, thickness)

        cv2.imshow("Video", img)  # показать
        key = cv2.waitKey(1)
        if key == 27:
            print("exit by key")
            break
    cv2.destroyWindow("Video") #разрушит окно

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)  # номер вебкамеры ноута - 0
    try:
        main(cap)
    finally:
        cap.release()  # отпустить камеру
    cv2.destroyAllWindows()