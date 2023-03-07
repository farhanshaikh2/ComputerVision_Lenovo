import cv2
import numpy as np
import matplotlib.pyplot as plt


def show_with_matplotlib(color_image, title, position):
    # Convert BGR image to RGB
    image_RGB = color_image[:, :, ::-1]

    ax = plt.subplot(3, 3, position)
    plt.imshow(image_RGB)
    plt.title(title)
    plt.axis('off')


# Create a figure() object with appropriate size and title.
plt.figure(figsize=(12, 6))
plt.suptitle("Smoothing techniques", fontsize=14, fontweight='bold')

image = cv2.imread('05_Image_processing_techniques\cat-face.png')

# we create a kernel for smoothing images.
# In this example we will use (10,10) kernel
kernel_avg_10_10 = np.ones((10, 10), np.float32)/100

# print(f"kernel {kernel_avg_10_10}")

# This function cv2.blur() smooths and image using the normalized box filter
smooth_image_b = cv2.blur(image, (10, 10))

show_with_matplotlib(image, "original", 1)
show_with_matplotlib(smooth_image_b, "cv2.blur", 2)

plt.show()
