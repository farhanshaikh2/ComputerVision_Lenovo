"""
Example to show how to draw basic shapes using OpenCV (2)
"""

# Import required packages:
import cv2
import numpy as np
import matplotlib.pyplot as plt


def show_with_matplotlib(img, title):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB:
    img_RGB = img[:, :, ::-1]

    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()


# Dictionary containing some colors:
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

# We create a canvas to draw 300 x 300 imagae with 3 channels.
image = np.zeros((300, 300, 3), dtype=np.uint8)

image[:] = colors['light_gray']

# 1. We are going to see how cv2.clipLine() works
# Draw a rectangle and a line:
# cv2.line(image, (0, 0), (300, 300), colors['green'], 3)
# cv2.rectangle(image, (0, 0), (100, 100), colors['blue'], 3)

ret, p1, p2 = cv2.clipLine((0, 0, 100, 100), (50, 50), (300, 300))


if ret:
    cv2.line(image, p1, p2, colors['yellow'], 3)


# show_with_matplotlib(image, "")

image[:] = colors['light_gray']

cv2.arrowedLine(image, (50, 50), (200, 50), colors['green'], 3, tipLength=0.05)
cv2.arrowedLine(image, (50, 120), (200, 120),
                colors['green'], 3, cv2.LINE_AA, 0, tipLength=0.1)

# show_with_matplotlib(image, "")image[:] = colors['light_gray']


image[:] = colors['light_gray']

# cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color,
# thickness=1, lineType=8, shift=0)

# cv2.ellipse(image, (80, 80), (60, 30), 0, 0, 360, colors['red'], -1)
# cv2.ellipse(image, (80, 200), (80, 40), 0, 0, 360, colors['green'], 3)
# cv2.ellipse(image, (80, 200), (10, 40), 0, 0, 360, colors['blue'], 3)
cv2.ellipse(image, (80, 200), (10, 40), 45, 0, 270, colors['green'], 3)
# cv2.ellipse(image, (80, 200), (50, 40), 0, 0, 360, colors['red'], 3)
# cv2.ellipse(image, (80, 200), (10, 50), 0, 0, 360, colors['cyan'], 3)


# show_with_matplotlib(image, "")

image[:] = colors['light_gray']

# These points define a triangle
pts = np.array([[250, 5], [220, 80], [280, 80]], dtype=np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(image, [pts], True, colors['green'], 3)

# # These points define a triangle
# pts = np.array([[250, 105], [220, 180], [280, 180]], dtype=np.int32)
# pts = pts.reshape(-1, 1, 2)
# cv2.polylines(image, [pts], True, colors['green'], 3)

# Draw a polygon with false option
pts = np.array([[250, 105], [220, 180], [280, 180]], dtype=np.int32)
pts = pts.reshape(-1, 1, 2)
cv2.polylines(image, [pts], False, colors['green'], 3)

pts = np.array([[20, 90], [60, 60], [100, 90], [80, 130], [40, 130]], np.int32)
pts = pts.reshape(-1, 1, 2)

print(pts.shape)
cv2.polylines(image, [pts], True, colors['blue'], 3)

show_with_matplotlib(image, "")
