import cv2
import random

img = cv2.imread('assets/logo.png',1) 
img = cv2.resize(img, (450,450))
#to change color of image at specific area 

print(img) #-> numpy array
print(img.shape) #-> returns [rows(height), col.(width), channels(color space of our image or how many values/colors are representing each pixel)
print(img[257][40]) #-> specific channel

for i in range(50): #all rows upto 100
	for j in range(img.shape[1]): #shape gives (rows,col,channel) so we get col
		img[i][j] = [random.randrange(255), random.randint(0, 255), random.randint(0, 255)] #random colors as a pixel contain 3 colors BGR

# copy and paste image(copy part of the array)
#copying the middle logo here 

tag = img[200:300, 100:200] #numpy arrays have double slicing (copied)
img[100:200, 200:300] = tag #paste



cv2.imshow('Image(window name)',img) 
cv2.waitKey(0)
cv2.destroyAllWindows()