import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def too_dark(fname):
    image_too_dark = Image.open(fname).convert("L")
    img_dark = np.asarray(image_too_dark)

    plt.figure(figsize=(15, 10))
    plt.suptitle('Przed korektą (obraz za ciemny)', fontsize=20)

    plt.subplot(2, 2, 1)
    plt.title('Mona Lisa')
    plt.imshow(img_dark, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 2, 2)
    plt.title("Histogram")
    plt.hist(img_dark)
    plt.show()

    plt.figure(figsize=(15, 10))
    plt.suptitle('Po korekcie', fontsize=20)

    plt.subplot(2, 2, 1)
    plt.title('Mona Lisa')
    img_dark_correction = cv2.equalizeHist(img_dark)  # wyrównywanie histogramu obrazu w skali szarości
    plt.imshow(img_dark_correction, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 2, 2)
    plt.title("Histogram")
    plt.hist(img_dark_correction)
    plt.show()


def too_bright(fname):
    image_too_bright = Image.open(fname).convert("L")
    img_bright = np.asarray(image_too_bright)

    plt.figure(figsize=(15, 10))
    plt.suptitle('Przed korektą (obraz za jasny)', fontsize=20)

    plt.subplot(2, 2, 1)
    plt.title('Bociany')
    plt.imshow(img_bright, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 2, 2)
    plt.title("Histogram")
    plt.hist(img_bright)
    plt.show()

    plt.figure(figsize=(15, 10))
    plt.suptitle('Po korekcie', fontsize=20)

    plt.subplot(2, 2, 1)
    plt.title('Bociany')
    img_bright_correction = cv2.equalizeHist(img_bright)  # wyrównywanie histogramu obrazu w skali szarości
    plt.imshow(img_bright_correction, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 2, 2)
    plt.title("Histogram")
    plt.hist(img_bright_correction)
    plt.show()


if __name__ == '__main__':
    #too_dark('dark_forest.jpg')
    too_bright('Bociany.jpg')
