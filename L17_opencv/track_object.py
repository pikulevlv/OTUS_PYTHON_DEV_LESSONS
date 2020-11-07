import cv2



def main(cap):

    while True:
        success, img = cap.read()
        if not success:
            print("Couldn't read frame")
            return

        cv2.imshow("Choose_frame", img)  # показать
        key = cv2.waitKey(5) # задержка 5 милисекунд
        if key == 27:
            print("exit by key")
            break
    cv2.destroyWindow("Choose_frame") #разрушит окно
    bbox = cv2.selectROI("Select", img) # для последнего кадра даст выбрать часть кадра
    # print(bbox)

    tracker = cv2.TrackerKCF_create()
    ok = tracker.init(img, bbox)
    print("Init:", ok)

    history = []
    frame_count = 0
    while True:
        success, img = cap.read()
        ok, (x, y, w, h) = tracker.update(img)
        if not success:
            print("Couldn't read frame")
            return



        if ok:
            if frame_count % 2 == 0:
                history.append((int(x), int(y), int(w), int(h)))
            pt1 = (int(x), int(y))  # upper left
            pt2 = (int(x) + int(w), int(y) + int(h))  # lower right
            B = int(x * w) % 255
            G = int(y * h) % 255
            color = (B, G, 255)
            thickness = 2
            print(pt1, pt2, color, thickness)
            cv2.rectangle(img, pt1, pt2, color, thickness)

        for (x, y, w, h) in history:
            w_center = w // 2
            h_center = h // 2
            pt1 = (x+w_center, y+h_center)  # upper left
            pt2 = (x+w_center+1, y+h_center+1)  # lower right
            B = int(x * w) % 255
            G = int(y * h) % 255
            color = (B, G, 255)
            thickness = 1
            print(pt1, pt2, color, thickness)
            cv2.rectangle(img, pt1, pt2, color, thickness)

        cv2.imshow("Tracking", img)  # показать

        key = cv2.waitKey(5)
        if key == 27:
            break
    cv2.destroyWindow("Tracking")

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)  # номер вебкамеры ноута - 0
    try:
        main(cap)
    finally:
        cap.release()  # отпустить камеру
    cv2.destroyAllWindows()