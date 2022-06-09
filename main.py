import cv2 as cv
import numpy as np
from os import system
from time import sleep


system('cls')

fpath = "images/kurapika.jpg"

img = cv.imread(fpath)


if len(img.shape) < 3:
    print("Image is grayscale")
    sleep(3)
    exit()


system('cls')
shp = img.shape
print("Access a pixel")
xCoord = int(input("Enter 'x' coordinate value (max value "+str(shp[0])+" ) : "))
yCoord = int(input("Enter 'y' coordinate value (max value "+str(shp[1])+" ) : "))
channel = int(input("""Select channel:
0 - blue
1 - green
2 - red
>> """))

accss = img.item(xCoord, yCoord, channel)


system('cls')
shp = img.shape
print("Modify a pixel")
xCoo = int(input("Enter 'x' coordinate value (max value "+str(shp[0])+" ) : "))
yCoo = int(input("Enter 'y' coordinate value (max value "+str(shp[1])+" ) : "))
bluchannel = int(input("Enter blue channel value: "))
greenchannel = int(input("Enter green channel value: "))
redchannel = int(input("Enter red channel value: "))

system('cls')

print("Outputs:")

print("\nAccessed Pixel Value:", accss)

print("Pixel value before modify:", img[xCoo, yCoo])

img.itemset((xCoo, yCoo, 0), bluchannel)
img.itemset((xCoo, yCoo, 1), greenchannel)
img.itemset((xCoo, yCoo, 2), redchannel)

print("Pixel value after modified:", img[xCoo, yCoo])  


wdth = 300
hght = 300

if wdth > shp[1] or hght > shp[0]:
    print("Set Image Dimension: Out of bounds")
else:
    print("Set Image Dimension: Within the bounds")



pixCount = 1683001

if pixCount > img.size: print("Set pixel: Higher than the pixel count")
elif pixCount < img.size: print("Set pixel: Lower than the pixel count")
else: print("Set pixel: Equal to the pixel count")

print("Image Data Type:", img.dtype)