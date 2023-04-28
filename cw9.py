import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def sobel():
    fname = 'zarzecze.jpg'
    image = Image.open(fname).convert("L")
    img_zarzecze = np.asarray(image)

    fname = 'trawlosc_pamieci.png'
    image = Image.open(fname).convert("L")
    img_pamiec = np.asarray(image)

    fname = 'house_under_construction.jpg'
    image = Image.open(fname).convert("L")
    img_house = np.asarray(image)

    plt.figure(figsize=(17, 12))

    plt.subplot(3, 3, 1)
    plt.imshow(img_zarzecze, cmap='gray', vmin=0, vmax=255)

    plt.subplot(3, 3, 2)
    plt.title("Sobel X")
    plt.imshow(cv2.Sobel(img_zarzecze, -1, 1, 0, ksize=3), cmap='gray', vmin=0, vmax=255)  # poziomy filtr Sobela

    plt.subplot(3, 3, 3)
    plt.title("Sobel Y")
    plt.imshow(cv2.Sobel(img_zarzecze, -1, 0, 1, ksize=3), cmap='gray', vmin=0, vmax=255)  # pionowy filtr Sobela

    plt.subplot(3, 3, 4)
    plt.imshow(img_pamiec, cmap='gray', vmin=0, vmax=255)

    plt.subplot(3, 3, 5)
    plt.title("Sobel X")
    plt.imshow(cv2.Sobel(img_pamiec, -1, 1, 0, ksize=3), cmap='gray', vmin=0, vmax=255)  # poziomy filtr Sobela

    plt.subplot(3, 3, 6)
    plt.title("Sobel Y")
    plt.imshow(cv2.Sobel(img_pamiec, -1, 0, 1, ksize=3), cmap='gray', vmin=0, vmax=255)  # pionowy filtr Sobela

    plt.subplot(3, 3, 7)
    plt.imshow(img_house, cmap='gray', vmin=0, vmax=255)

    plt.subplot(3, 3, 8)
    plt.title("Sobel X")
    plt.imshow(cv2.Sobel(img_house, -1, 1, 0, ksize=3), cmap='gray', vmin=0, vmax=255)  # poziomy filtr Sobela

    plt.subplot(3, 3, 9)
    plt.title("Sobel Y")
    plt.imshow(cv2.Sobel(img_house, -1, 0, 1, ksize=3), cmap='gray', vmin=0, vmax=255)  # pionowy filtr Sobela
    plt.show()


def laplace():
    fname = 'zarzecze.jpg'
    image = Image.open(fname).convert("L")
    img_zarzecze = np.asarray(image)

    fname = 'trawlosc_pamieci.png'
    image = Image.open(fname).convert("L")
    img_pamiec = np.asarray(image)

    fname = 'house_under_construction.jpg'
    image = Image.open(fname).convert("L")
    img_house = np.asarray(image)

    plt.figure(figsize=(17, 12))

    plt.subplot(3, 4, 1)
    plt.imshow(img_zarzecze, cmap='gray', vmin=0, vmax=255)

    plt.subplot(3, 4, 5)
    plt.imshow(img_pamiec, cmap='gray', vmin=0, vmax=255)

    plt.subplot(3, 4, 9)
    plt.imshow(img_house, cmap='gray', vmin=0, vmax=255)

    plt.subplot(3, 4, 2)
    plt.title("Maska 3x3")
    plt.imshow(cv2.Laplacian(img_zarzecze, -1, ksize=3), cmap='gray', vmin=0, vmax=255)  # maska Laplace'a 3x3

    plt.subplot(3, 4, 3)
    plt.title("Maska 5x5")
    plt.imshow(cv2.Laplacian(img_zarzecze, -1, ksize=5), cmap='gray', vmin=0, vmax=255)  # maska Laplace'a 5x5

    plt.subplot(3, 4, 4)
    plt.title("Maska 11x11")
    plt.imshow(cv2.Laplacian(img_zarzecze, -1, ksize=11), cmap='gray', vmin=0, vmax=255)  # maska Laplace'a 11x11

    plt.subplot(3, 4, 6)
    plt.title("Maska 3x3")
    plt.imshow(cv2.Laplacian(img_pamiec, -1, ksize=3), cmap='gray', vmin=0, vmax=255)  # maska Laplace'a 3x3

    plt.subplot(3, 4, 7)
    plt.title("Maska 5x5")
    plt.imshow(cv2.Laplacian(img_pamiec, -1, ksize=5), cmap='gray', vmin=0, vmax=255)  # maska Laplace'a 5x5

    plt.subplot(3, 4, 8)
    plt.title("Maska 11x11")
    plt.imshow(cv2.Laplacian(img_pamiec, -1, ksize=11), cmap='gray', vmin=0, vmax=255)  # maska Laplace'a 11x11

    plt.subplot(3, 4, 10)
    plt.title("Maska 3x3")
    plt.imshow(cv2.Laplacian(img_house, -1, ksize=3), cmap='gray', vmin=0, vmax=255)  # maska Laplace'a 3x3

    plt.subplot(3, 4, 11)
    plt.title("Maska 5x5")
    plt.imshow(cv2.Laplacian(img_house, -1, ksize=5), cmap='gray', vmin=0, vmax=255)  # maska Laplace'a 5x5

    plt.subplot(3, 4, 12)
    plt.title("Maska 11x11")
    plt.imshow(cv2.Laplacian(img_house, -1, ksize=11), cmap='gray', vmin=0, vmax=255)  # maska Laplace'a 11x11
    plt.show()


if __name__ == '__main__':
    sobel()
    laplace()
