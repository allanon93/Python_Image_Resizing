import cv2
import glob


images = glob.glob("*jpg")

for image in images:
    img = cv2.imread(image, 1)
    re_img = cv2.resize(img, (100, 100))
    cv2.imshow("Hey", re_img)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_" + image, re_img)