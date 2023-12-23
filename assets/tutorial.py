# color mods
# -1 -> cv2.IMREAD_COLOR : Loads color image. any transparency of image will be neglected(default)
# 0  -> cv2.IMREAD_GRAYSCALE : Loads image in grayscale.
# 1  -> cv2.IMREAD_UNCHANGED : Loads image including alpha channel(i.e. if image color has transparency then it will honour it)
import cv2

img = cv2.imread('assets/logo.png',1) # (path, color mod) -> parameters 

cv2.imshow('Image(window name)',img)  # (winname that will show up on opening, image name to be proccessed)
cv2.waitKey(0) # 0 -> means it will wait infinite time until we press a key but if 5 then 5sec wait and auto shut
cv2.destroyAllWindows() # destroy all windows after pressing any key
