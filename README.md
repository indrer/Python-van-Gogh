# Python van Gogh

A simple Python script to recreate given images.
Takes an image and creates two images of the same size. Then picks a random color from the original image and draws a line of that of random length and width on first image. If first image is more like the original, overwrites the second image with the contents of first image, and vice versa.

The script takes roughly 30 minutes to execute 1 mil iterations when logging is enabled and an image is of size 400x400. Larger images might take longer as the size of drawn lines depend on the size of an image. 

Script in action:

![Progress](https://github.com/u-pi/Python-van-Gogh/blob/master/progress.gif) ![Original](https://github.com/u-pi/Python-van-Gogh/blob/master/rdj.jpg)

## Installation
In order to use this script you need to have the following installed:
- Python 3 (tested on Python 3.7.0)
- Pillow (pip install Pillow)

Then simply download the script or clone this repo.

## Usage
1. Download or clone this repo to your local machine.
2. cd into the Python-van-Gogh folder (cd path/to/Python-van-Gogh)
3. Run the script:

```
python3 main.py
```

When the script is running:
- You will be asked to input number of iterations (recommended more than 5000).
- You will be asked to input a path to an image 

If the image is in the Python-van-Gogh folder you can simply provide the filename with extension (eg. rdj.jpg) or an absolute path (eg. /Users/myusername/Desktop/img.png)
