import cv2
import numpy as np
import matplotlib.pyplot as plt


def show_with_matplotlib(image, title):
    image_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.imshow(image_RGB)
    plt.title(title)
    plt.show()


# Dictionary containing some colors:
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

# We create the canvas to draw: 400 x 400 pixels, 3 channels, uint8 (8-bit unsigned integers)
# We set the background to black using np.zeros():
image = np.zeros((400, 400, 3), dtype=np.uint8)


image[:] = colors['light_gray']


# We are going to see how cv2.line() works:
cv2.line(image, (0, 0), (400, 400), colors['green'], 3)
cv2.line(image, (0, 400), (400, 0), colors['blue'], 3)
cv2.line(image, (200, 0), (200, 400), colors['red'], 10)
cv2.line(image, (0, 200), (400, 200), colors['yellow'], 10)

# show image
# show_with_matplotlib(image, "cv2.line()")

# Make canvas to draw again
image[:] = colors['light_gray']

# Now we will see how cv2.rectangle() works:
cv2.rectangle(image, (10, 50), (60, 300),
              colors['green'], 3, lineType=8, shift=0)
cv2.rectangle(image, (80, 50), (130, 300), colors['blue'], -1)
cv2.rectangle(image, (150, 50), (350, 100), colors['red'], -1)
cv2.rectangle(image, (150, 150), (350, 300), colors['cyan'], 10)


# show image
# show_with_matplotlib(image, "cv2.rectangle()")

# Create a new blank canvas
image[:] = colors['light_gray']

cv2.circle(image, (50, 50), 20, colors['green'], 3)
cv2.circle(image, (100, 100), 30, colors['blue'], -1)
cv2.circle(image, (200, 200), 40, colors['magenta'], 10)
cv2.circle(image, (300, 300), 40, colors['cyan'], -1)

# show image
show_with_matplotlib(image, "cv2.circle()")
