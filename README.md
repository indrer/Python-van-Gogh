# Python van Gogh

A simple Python script to recreate given images.
Takes an image and creates two images of the same size. Then picks a random color from the original image and draws a line of that of random length and width on first image. If first image is more like the original, overwrites the second image with the contents of first image, and vice versa.

The script takes roughly 30 minutes to execute 1 mil iterations when logging is enabled and an image is of size 400x400. Larger images might take longer as the size of drawn lines depend on the size of an image. 

Script in action:

![Progress](https://github.com/u-pi/Python-van-Gogh/blob/master/progress.gif) ![Original](https://github.com/u-pi/Python-van-Gogh/blob/master/rdj.jpg)
