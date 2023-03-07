import cv2
import matplotlib.pyplot as plt


def show_with_matplotlib(image, title, pos):
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    ax = plt.subplot(3, 6, pos)
    plt.imshow(img_rgb)
    plt.title(title)
    plt.axis('off')


# Load the original image:
image = cv2.imread('05_Image_processing_techniques\color_spaces.png')

plt.figure(figsize=(13, 5))
plt.suptitle("Splitting and merging channels in opencv",
             fontsize=14, fontweight='bold')

show_with_matplotlib(image, "BGR - image", 1)

b, g, r = cv2.split(image)


# show all the channels from BGR image:
show_with_matplotlib(cv2.cvtColor(b, cv2.COLOR_GRAY2BGR), "BGR - (B)", 2)
# show_with_matplotlib(cv2.cvtColor(g, cv2.COLOR_GRAY2BGR), "BGR - (G)", 2+6)
# show_with_matplotlib(cv2.cvtColor(r, cv2.COLOR_GRAY2BGR), "BGR - (R)", 2+6*2)

# image_copy = cv2.merge((b,  g, r))

# show_with_matplotlib(image_copy, "BGR - image (copy)", 1+6)

# blue_copy = image[:, :, 0]
# green_copy = image[:, :, 1]
# red_copy = image[:, :, 2]

# # image without blue
# image_without_blue = image.copy()
# image_without_blue[:, :, 0] = 0

# # image without green
# image_without_green = image.copy()
# image_without_green[:, :, 1] = 0

# # image without red
# image_without_red = image.copy()
# image_without_red[:, :, 2] = 0

# show_with_matplotlib(image_without_blue,
#                      "BGR_without - (B)", 3)
# show_with_matplotlib(image_without_green,
#                      "BGR_without - (G)", 3+6)
# show_with_matplotlib(image_without_red,
#                      "BGR_without - (B)", 3+6*2)


# b, g, r = cv2.split(image_without_blue)

# # Show all the channels from the BGR image without the blue information:
# show_with_matplotlib(cv2.cvtColor(b, cv2.COLOR_GRAY2BGR),
#                      "BGR without B (B)", 4)
# show_with_matplotlib(cv2.cvtColor(g, cv2.COLOR_GRAY2BGR),
#                      "BGR without B (G)", 4 + 6)
# show_with_matplotlib(cv2.cvtColor(r, cv2.COLOR_GRAY2BGR),
#                      "BGR without B (R)", 4 + 6 * 2)

plt.show()
