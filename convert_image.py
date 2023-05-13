"""
convert_image
Get all files en raw, resize to 608x608 and write 
with new name in converted
 ...

Attributes
----------

down_width : int
        value to resize width, yolo default 608
down_height : int
        value to resize height, yolo default 608
path_raw : string
        directory name for source image, default ./raw
path_converted : string
        diretory name with images resized, default '../converted/'

Whot to use:
------------

python convert_image.py

Author:
------
André Eppinghaus

References: 
----------
 - https://learnopencv.com/image-resizing-with-opencv/
 - https://docs.python.org/3/library/os.html
 - https://docs.opencv.org/4.x/
 - https://realpython.com/documenting-python-code/

"""
import os
import cv2
import numpy as np

#
# Resolution for yolo
#
down_width = 608
down_height = 608
path_raw = 'raw'
path_converted='../converted/'
# cd raw
os.chdir(path_raw)

#list files
files_path = [os.path.abspath(x) for x in os.listdir()]
count=1

for file in files_path:
    print('\n File read: '+file)
    filename_converted=path_converted+str(count)+'.jpeg'

    # Read the image using imread function
    image = cv2.imread(file)
    # cv2.imshow('Original Image', image)
    # break
 
    # let's downscale the image using new  width and height
    down_points = (down_width, down_height)
    resized = cv2.resize(image, down_points, interpolation= cv2.INTER_LINEAR)
    cv2.imwrite(filename_converted, resized)
    print('\n File writed: '+filename_converted)
    count = count + 1

