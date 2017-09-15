#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 21:55:27 2017

@author: ChrisErnst

Examples below come from "Programming Computer Vision with Python
by Jan Erik Solem
"""

# Chapter 1: Basic Image Handling and Processing

import os
from PIL import Image
from pylab import *
import numpy as np
import matplotlib.pyplot as plt


os.chdir('/Users/ChrisErnst/Development/Python/Image_Manipulation')

pil_im = array(Image.open('chrysler.jpg'))
# Prepares the image in original form
imshow(pil_im)
# Shows the image in a new window

heat_im = Image.open('chrysler.jpg').convert('L')
# Converts to heatmap like image
imshow(heat_im)

gray_im = Image.open('chrysler.jpg').convert('LA')
# Converts to grayscale
imshow(gray_im)

gray_im.save('grayChrysler.png')
# Saves gray image as a png

#pil_im.thumbnail((128,128))
# Creates a thumbnail

box = (600,800,800,1000)
region = pil_im.crop(box)
# Takes positional arguments (left, upper, right, lower)
imshow(region)

region.rotate(90)
# Rotates by 90 deg
region =  region.transpose(Image.ROTATE_180)
imshow(region)
region.save('rotatedRegion.jpg')
# Rotates by 90 deg

pil_im.paste(region, box)
imshow(pil_im)
# Cuts out the region, flips it and pastes it upsidedown
pil_im.paste(region, (100, 800, 300, 1000))
imshow(pil_im)
# Cuts out the region, flips it and pastes it upsidedown to the left

out = pil_im.resize((128,128))
imshow(out)
# Resizes to 128, 128 pixels


# Conduct grayscale conversion on the pixels
shape(pil_im)
# Returns (200,1424, 3): meaning the image is 2000 x 1424, and has 3 values per pixels(RGB)

# Grayscale conversion: Y = 0.299*R + 0.587*G + 0.114*B 

R = pil_im[:,:,0]
G = pil_im[:,:,1]
B = pil_im[:,:,2]

gray_pil_im = 0.299*R + 0.587*G + 0.114*B 
shape(gray_pil_im)
imshow(gray_pil_im)

plt.figure()
plt.gray()
gryChrysler = plt.contour(gray_pil_im, origin='image')
axis('equal')
axis('off')
plt.savefig('grayContourChrysler.png')
# Contours the Chrysler photo

# color List = b,g,r,c,m,y,k,w


