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
def save_subimage(image, x1, y1, x2, y2, file_path):
    subimage = image[x1:x2, y1:y2]
    cv2.imwrite(file_path, subimage)


def point_transformation(file_path, file_path_gray, new_level):
    # Load the image
    image = Image.open(file_path)
    # Convert the image to grayscale
    grayscale_image = image.convert('L')
    # Change the level of grayscale
    grayscale_image = grayscale_image.point(lambda x: x * (new_level / 255))
    # Save the new image
    grayscale_image.save(file_path_gray)


def contrast_transformation(file_path, file_path_contrast, factor):
    # Load the image
    image = Image.open(file_path)
    #grayscale_image = image.convert('L')
    # Apply the contrast function to each pixel
    contrast_image = image.point(lambda c: contrast(c, factor))
    # Save the new image
    contrast_image.save(file_path_contrast)


# Create a contrast function
def contrast(c, factor):
    return 128 + factor * (c - 128)
    # return 1 / (1 + (m / c) ** e)


def gamma_transformation(file_path, file_path_gamma, gamma):
    # Load the image
    image = Image.open(file_path)
    # Convert the image to a numpy array
    image_array = np.array(image)
    # Normalize the pixel values between 0 and 1
    image_array_normalized = image_array / 255.0
    image_array_corrected = np.power(image_array_normalized, gamma)
    # Convert the numpy array back to an image
    new_image = Image.fromarray(np.uint8(image_array_corrected * 255))
    # Save the new image
    new_image.save(file_path_gamma)


def zad1():
    # Przykładowe użycie funkcji
    image = load_image("obraz.jpg")
    show_image(image, "Obraz")

    plot_gray_levels(image, x=100)
    plot_gray_levels(image, y=100)

    save_subimage(image, 100, 100, 200, 200, "podobraz.jpg")


def zad2():
    point_transformation("obraz.jpg", "obraz_gray.jpg", 200)
    contrast_transformation("obraz.jpg", "obraz_contrast.jpg", 1.5)
    gamma_transformation("obraz.jpg", "obraz_gamma.jpg", 0.5)


if __name__ == '__main__':
    # zad1()
    zad2()
