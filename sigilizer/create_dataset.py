import os
import cv2

# Make sure only b,g,r channels are available

root = './sigils/'
images = os.listdir(root)
for image in images:
  if not image.startswith('.'):
    try:
      img = cv2.imread(root + image)
      b, g, r = cv2.split(img)
      img = cv2.cvtColor(cv2.merge([r, g, b]), cv2.COLOR_BGR2GRAY)
      cv2.imwrite('DCGAN-tensorflow/data/sigils-bw/' + image, img)
    except:
      print('Error for:', root+image)
