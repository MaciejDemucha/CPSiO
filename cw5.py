import matplotlib.pyplot as plt  # import biblioteki MatPlotLib
import numpy as np  # import biblioteki NumPy
from PIL import Image  # import biblioteki Pillow

if __name__ == '__main__':
    fname = 'obraz.jpg'  # nazwa pliku
    y1 = 0
    y2 = 150
    x1 = 0
    x2 = 300
    image_color = Image.open(fname)  # otwarcie i indentyfikacja obrazu
    img_color = np.asarray(image_color)  # konwersja obrazu w tablicę
    plt.imshow(img_color)  # wyświetlenie tablicy jako zdjęcia
    #plt.show()

    image_grayscale = Image.open(fname).convert("L")  # convert("L") - konwersja zdjęcia do skali szarości
    img_gray = np.asarray(image_grayscale)

    plt.figure(figsize=(15, 10))  # tworzenie nowej figury o rozmiarach podanych w calach

    plt.subplot(1, 2, 1)  # dodanie podwykresu do figury
    plt.title('Obraz')  # dodanie tytułu podwykresu
    plt.imshow(img_gray, cmap='gray', vmin=0,
               vmax=255)  # cmap - mapa kolorów, vmin i vmax - zakres, który obejmuje mapa kolorów.

    plt.subplot(1, 2, 2)
    plt.title('Histogram')
    plt.hist(img_gray)  # wykreślanie histogramu na podstawie danych w tablicy
    plt.show()

    img_cropped = img_gray[y1:y2, x1:x2]  # przypisanie zmiennej img_cropped części talibicy img_gray
    plt.imshow(img_cropped, cmap='gray', vmin=0, vmax=255)
    plt.show()  # zapisanie figury
