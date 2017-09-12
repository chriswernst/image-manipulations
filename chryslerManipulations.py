#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 21:55:27 2017

@author: ChrisErnst
"""

import os

from PIL import Image
from pylab import *

os.chdir('/Users/ChrisErnst/Development/Python/Image_Manipulation')

pil_im = Image.open('chrysler.jpg')
# Prepares the image in original form

heat_im = Image.open('chrysler.jpg').convert('L')
# converts to heatmap like image

grey_im = Image.open('chrysler.jpg').convert('LA')
# converts to greyscale

imshow(pil_im)
# shows the image in a new window

grey_im.save('greyChrysler.png')
# saves grey image as a png

pil_im.thumbnail((100,100))

box = (300,300,800,800)
region = pil_im.crop(box)
imshow(region)
# Crops a specific portion of the image

region.rotate(90)
# Rotates by 90 deg