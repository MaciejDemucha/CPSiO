import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


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
    # grayscale_image = image.convert('L')
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

    plt.savefig("obraz_stala.jpg")


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

    plt.savefig("obraz_contrast.jpg")


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

    plt.savefig("obraz_gamma.jpg")


if __name__ == '__main__':
    fname = "obraz.jpg"
    image_grayscale = Image.open(fname).convert("L")
    image_gray = np.asarray(image_grayscale)
    constant_transform(image_gray)
    contrast_transform(image_gray)
    gamma_transform(image_gray)
