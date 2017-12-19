import cv2
import numpy as np

img = cv2.imread('DCGAN-tensorflow/samples/test_arange_25.png', 0)

def show(blurred):
  stacked = np.hstack((img, blurred))
  cv2.imshow('img', stacked)
  cv2.waitKey(0)

# replaces pixel value with kernel function (ex: mean) of neighbors that are underneath the kernel window
# (5, 5) == size of kernel window

blur = cv2.blur(img, (5, 5))
print('box')
show(blur)

gaussian = cv2.GaussianBlur(img, (5, 5), 0)
print('gaussian')
show(gaussian)

median = cv2.medianBlur(img, 5)
print('median')
show(median)

# good at preserving edges
blur = cv2.bilateralFilter(img, 9, 75, 75)
print('bilateral')
show(blur)

blur_median = cv2.medianBlur(cv2.bilateralFilter(img, 9, 75, 75), 5)
print('bilateral + median')
show(blur_median)

blur_median_inverse = cv2.bilateralFilter(cv2.medianBlur(img, 5), 9, 75, 75)
print('median + bilateral')
show(blur_median_inverse)

# makes sure pixel histogram of image (distribution of pixel values) is more uniform
equalized = cv2.equalizeHist(img)
print('equalized histogram')
show(equalized)

# histogram equalization but less extreme to preserve some details
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_img = clahe.apply(img)
print('adaptive histogram equalization')
show(clahe_img)

# blurring is local (neighboring pixels). denoising takes into account global image.
# take pixel, small area around pixel, and look for similar areas in image. then
# replace pixel value with mean of all those areas. 10 is recommended filter strength
# (the higher, the more it removes noise, but also removes details). Recommended template
# window size is 7. Recommended search window size is 21.
denoised = cv2.fastNlMeansDenoising(img, None, 30, 7, 21)
print('denoising')
show(denoised)
