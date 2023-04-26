import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def linear_filter(fname):
    image = Image.open(fname).convert("L")
    img = np.asarray(image)

    plt.figure(figsize=(15, 10))

    plt.subplot(2, 2, 1)
    plt.title("Obraz oryginalny")
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 2, 2)
    plt.title("Maska 3x3")
    plt.imshow(cv2.blur(img, (3, 3)), cmap='gray', vmin=0, vmax=255)  # cv. blur() - maska 3x3

    plt.subplot(2, 2, 3)
    plt.title("Maska 7x7")
    plt.imshow(cv2.blur(img, (7, 7)), cmap='gray', vmin=0, vmax=255)  # cv. blur() - maska 7x7

    plt.subplot(2, 2, 4)
    plt.title("Maska 15x15")
    plt.imshow(cv2.blur(img, (15, 15)), cmap='gray', vmin=0, vmax=255)  # cv. blur() - maska 15x15
    plt.show()


def non_linear_filter(fname):
    image = Image.open(fname).convert("L")
    img = np.asarray(image)

    plt.figure(figsize=(15, 10))

    plt.subplot(2, 2, 1)
    plt.title("Obraz oryginalny")
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 2, 2)
    plt.title("Maska 3x3")
    plt.imshow(cv2.medianBlur(img, 3), cmap='gray', vmin=0, vmax=255)  # cv.medianBlur() - maska 3x3

    plt.subplot(2, 2, 3)
    plt.title("Maska 7x7")
    plt.imshow(cv2.medianBlur(img, 7), cmap='gray', vmin=0, vmax=255)  # cv.medianBlur() - maska 7x7

    plt.subplot(2, 2, 4)
    plt.title("Maska 15x15")
    plt.imshow(cv2.medianBlur(img, 15), cmap='gray', vmin=0, vmax=255)  # cv.medianBlur() - maska 15X15
    plt.show()


if __name__ == '__main__':
    linear_filter("plane.png")
    non_linear_filter("plane.png")
