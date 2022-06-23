import numpy as np
import cv2
import os
import glob

img_path = '/Users/melvinwevers/Downloads/wetransfer_ubakzl12a5_008-jpg_2022-01-17_0858/*.jpg'


def make_tile(img, filename_, n_rows, n_cols):
    height = int(img.shape[0] / n_rows)
    width = int(img.shape[1] / n_cols)
    for row in range(n_rows):
        for col in range(n_cols):
            y0 = row * height
            y1 = y0 + height
            x0 = col * width
            x1 = x0 + width
            cv2.imwrite(f'{filename_}_{row}_{col}.jpg',  img[y0:y1, x0:x1])

imgs = glob.glob(img_path)
print(imgs)

for img in imgs:
    print(img)
    filename = os.path.basename(img)
    img = cv2.imread(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #make greyscale
    make_tile(img, filename, 4, 4)




