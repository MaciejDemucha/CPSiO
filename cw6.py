import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def constant_transform(img_gray):
    plt.figure(figsize=(15, 10))

    plt.subplot(2, 2, 1)
    plt.title('c = 1')
    plt.imshow(img_gray, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 2, 2)
    plt.title('c = 2')
    plt.imshow(cv2.multiply(img_gray, 2), cmap='gray', vmin=0,
               vmax=255)  # mnożenie tablicy/macieży przez skalar (c = 2)

    plt.subplot(2, 2, 3)
    plt.title('c = 4')
    plt.imshow(cv2.multiply(img_gray, 4), cmap='gray', vmin=0,
               vmax=255)  # mnożenie tablicy/macieży przez skalar (c = 4)

    plt.subplot(2, 2, 4)
    plt.title('c = 10')
    plt.imshow(cv2.multiply(img_gray, 10), cmap='gray', vmin=0,
               vmax=255)  # mnożenie tablicy/macieży przez skalar (c = 10)

    plt.show()


def contrast_transform(img_gray):
    plt.figure(figsize=(15, 10))

    plt.subplot(2, 2, 1)
    plt.title('m = 0.45, e = 8')
    img_contrast = (255 / (1 + np.power(0.45 / (img_gray / 255.0), 8)))  # modyfikacja równania w celu zapewnienia,
    # że liczby w img_contrast będą z zakresu 0-255
    plt.imshow(img_contrast, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 2, 2)
    plt.title('m = 0.2, e = 16')
    img_contrast = (255 / (1 + np.power(0.2 / (img_gray / 255.0), 16)))  # modyfikacja równania w celu zapewnienia,
    # że liczby w img_contrast będą z zakresu 0-255
    plt.imshow(img_contrast, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 2, 3)
    plt.title('m = 0.05, e = 2')
    img_contrast = (255 / (1 + np.power(0.05 / (img_gray / 255.0), 2)))  # modyfikacja równania w celu zapewnienia,
    # że liczby w img_contrast będą z zakresu 0-255
    plt.imshow(img_contrast, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 2, 4)
    plt.title('m = 0.01, e = 12')
    img_contrast = (255 / (1 + np.power(0.01 / (img_gray / 255.0), 12)))  # modyfikacja równania w celu zapewnienia,
    # że liczby w img_contrast będą z zakresu 0-255
    plt.imshow(img_contrast, cmap='gray', vmin=0, vmax=255)

    plt.show()


def gamma_transform(img_gray):
    plt.figure(figsize=(15, 10))

    plt.subplot(2, 2, 1)
    plt.title('c = 1.5, y = 3')
    img_gamma = 255 * 1.5 * np.power(img_gray / 255, 3);  # modyfikacja równania w celu zapewnienia,
    # że liczby w img_gamma będą z zakresu 0-255
    plt.imshow(img_gamma, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 2, 2)
    plt.title('c = 2, y = 0.5')
    img_gamma = 255 * 2 * np.power(img_gray / 255, 0.5);  # modyfikacja równania w celu zapewnienia,
    # że liczby w img_gamma będą z zakresu 0-255
    plt.imshow(img_gamma, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 2, 3)
    plt.title('c = 0.8, y = 0.8')
    img_gamma = 255 * 0.8 * np.power(img_gray / 255, 0.8);  # modyfikacja równania w celu zapewnienia,
    # że liczby w img_gamma będą z zakresu 0-255
    plt.imshow(img_gamma, cmap='gray', vmin=0, vmax=255)

    plt.subplot(2, 2, 4)
    plt.title('c = 1.5, y = 1')
    img_gamma = 255 * 1.5 * np.power(img_gray / 255, 1);  # modyfikacja równania w celu zapewnienia,
    # że liczby w img_gamma będą z zakresu 0-255
    plt.imshow(img_gamma, cmap='gray', vmin=0, vmax=255)

    plt.show()


if __name__ == '__main__':
    fname = "obraz.jpg"
    image_grayscale = Image.open(fname).convert("L")
    image_gray = np.asarray(image_grayscale)
    constant_transform(image_gray)
    contrast_transform(image_gray)
    gamma_transform(image_gray)
