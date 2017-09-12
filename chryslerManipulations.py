#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 21:55:27 2017

@author: ChrisErnst
"""

import os

from PIL import Image
from pylab import *

os.chdir('/Users/ChrisErnst/')

pil_im = Image.open('chrysler.jpg')
# Prepares the image in original form

pil_im = Image.open('chrysler.jpg').convert('l')

imshow(pil_im)