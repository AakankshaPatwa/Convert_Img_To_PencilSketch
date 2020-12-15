# -*- coding: utf-8 -*-
"""
#This program converts an image to a pencil sketch
@author: aakanksha
"""
import cv2

img_location = ''
filename = 'cute_puppies.jpg'
# Read in the image
img = cv2.imread(img_location + filename)

# Convert the image to gray scale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Invert the image
inverted_gray_image = 255 - gray_image

#Blur image by guassian function
blurred_img = cv2.GaussianBlur(inverted_gray_image, (21,21), 0)

#INVERT THE IMAGE
inverted_blurred_img = 255 - blurred_img

#Create the pencil sketch image
pencil_sketch_IMG = cv2.divide(gray_image, inverted_blurred_img, scale=256.0)

# Show the image
cv2.imshow('Original Image', img)
cv2.imshow('New Image', pencil_sketch_IMG)
cv2.waitKey(0)

