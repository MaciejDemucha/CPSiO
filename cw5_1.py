import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
from PIL import Image


# Funkcja wczytująca obraz z pliku
def load_image(file_path):
    img = cv2.imread(file_path)
    if img is None:
        print('Failed to load image file:')
        sys.exit(1)
    return img


# Funkcja wyświetlająca obraz
def show_image(image, title="Image"):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Funkcja wyświetlająca wykres zmian poziomu szarości wzdłuż wybranej linii poziomej lub pionowej
def plot_gray_levels(image, x=None, y=None):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # plt.imshow(image)
    if x is not None:
        line = gray_image[x, :]
        plt.plot(line)
        plt.show()
    elif y is not None:
        line = gray_image[:, y]
        plt.plot(line)
        plt.show()
    else:
        print("Nie wybrano linii.")


# Funkcja zapisująca podobraz o podanych współrzędnych do pliku
def save_subimage(img_name, x1, y1, x2, y2, file_path):
    subimage = img_name[x1:x2, y1:y2]
    cv2.imwrite(file_path, subimage)
    created_subimage = load_image(file_path)
    show_image(created_subimage)


if __name__ == '__main__':
    # Przykładowe użycie funkcji
    image = load_image("obraz.jpg")
    show_image(image)

    plot_gray_levels(image, x=100)
    plot_gray_levels(image, y=100)

    save_subimage(image, 0, 0, 100, 600, "podobraz.jpg")
