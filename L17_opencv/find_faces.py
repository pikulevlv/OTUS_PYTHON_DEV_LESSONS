import cv2
FRONTAL_FACE = "haarcascade_frontalface_default.xml"
IMAGE = 'image-2.jpg'
# создаем БД
faces_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + FRONTAL_FACE)


# print(img.shape)
# print(img.ndim)
def main():
    img = cv2.imread(IMAGE)
    # print(img.shape)
    # print(img)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # print(img_gray.shape)
    # print(img_gray)
    faces = faces_cascade_db.detectMultiScale(img_gray)
    # print(faces.shape) # (13, 4)- 13 лиц, 4 кооринаты (x,y,width,height)
    for i, (x, y, w, h) in enumerate(faces):
        pt1 = (x, y)# upper left
        pt2 = (x + w, y + h) # lower right
        B = (i * 10 + int(x) * i) % 255
        G = (i * 25 + int(y) * i) % 255
        color = (B, G, 255)
        thickness = 2
        cv2.rectangle(img, pt1, pt2, color, thickness)

    cv2.imshow("Image", img) #показать
    cv2.imwrite('IMG.jpg', img)
    while True:
        key = cv2.waitKey(0)
        if key == ord("q"):
            print("exit by key")
            break
    cv2.destroyWindow("Image") #разрушит окно

if __name__ == '__main__':
    main()
    cv2.destroyAllWindows()