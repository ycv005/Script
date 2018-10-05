''' Script to resize all files in current working directory,
    saving new .jpg and .jpeg images in a new folder. '''

import cv2
import glob         #looking for a file with a name or particular prefix/sufix or extension, glob will be helpful there
import os

imgs = glob.glob('*.jpg')   # *(wildcard or asterisk) is operator use to find out xxxxx.jpg file, it return a list

''' for multi level search - glob.glob("/home/user/*/*.txt")'''

imgs.extend(glob.glob('*.jpeg'))        #including the element of the list return
# print(imgs)

width = 28       #change it as your need
height = 28         #change it as your need

folder = 'resized'      #new folder with name resized
if not os.path.exists(folder):  #if this folder doesn't exists in the current directory then new folder is created
    os.makedirs(folder)

# Iterate through resizing and saving
for img in imgs:        #iterating via the list of the images.accordingly
    pic = cv2.imread(img, cv2.IMREAD_UNCHANGED)
    pic = cv2.resize(pic, (width, height))
    # print(img)
    cv2.imwrite(folder + '/' + img, pic)