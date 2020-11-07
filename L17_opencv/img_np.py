import cv2
import numpy as np

SHAPE = (480, 640, 3)

def main():
    img = np.zeros(SHAPE, dtype=np.uint8)
    img[..., [2]] = 255
    print(img)
    print(img.shape)

    cv2.imshow("Red image", img) #показать
    while True:
        key = cv2.waitKey(0)
        if key == ord("q"):
            print("exit by key")
            break

    cv2.destroyWindow("Red image") #разрушит окно

if __name__ == '__main__':
    main()