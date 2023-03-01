import cv2
import numpy as np
import matplotlib.pyplot as plt
import constant

print(f"red: {constant.RED}")


def show_with_matplotlob(image, title):
    image_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.imshow(image_RGB)
    plt.title(title)
    plt.show()


# Dictionary containing some colors:
colors = {'blue': (255, 0, 0),
          'green': (0, 255, 0),
          'red': (0, 0, 255),
          'yellow': (0, 255, 255),
          'magenta': (255, 0, 255),
          'cyan': (255, 255, 0),
          'white': (255, 255, 255),
          'black': (0, 0, 0),
          'gray': (125, 125, 125),
          'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50),
          'light_gray': (220, 220, 220)}
