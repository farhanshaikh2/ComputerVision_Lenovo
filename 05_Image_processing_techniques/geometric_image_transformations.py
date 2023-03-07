import cv2
import numpy as np
import matplotlib.pyplot as plt


def show_with_matplotlib(image, title):
    """Shows an image using matplotlib capabilities"""

    # Convert BGR image to RGB
    img_RGB = image[:, :, ::-1]

    # Show the image using matplotlib:
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()


image = cv2.imread('05_Image_processing_techniques\lena_image.png')

# show_with_matplotlib(image, "Original Image")

# 1. Scaling or resizing
# Resize the input image using cv2.resize()
# Resize using the scaling factor for each dimension of the image
# In this case the scaling factor is 0.5 in every dimension

dst_image = cv2.resize(image, None, fx=0.5, fy=0.5,
                       interpolation=cv2.INTER_AREA)

# show_with_matplotlib(dst_image, 'Resized image')

# Get the height and width of the image
height, width = image.shape[:2]

dst_image_2 = cv2.resize(image, (width*2, height*2),
                         interpolation=cv2.INTER_LINEAR)

# show_with_matplotlib(dst_image_2, 'Resized image 2')

# 2. Translation
# you need to create the 2x3 transformation matrix making use of numpy array with float values
M = np.float32([[1, 0, 100], [0, 1, 30]])

# dst_image = cv2.warpAffine(image, M, (width, height))

# show_with_matplotlib(dst_image, 'Warp Affine')

# Translation can take negative value as well.
M = np.float32([[1, 0, -100], [0, 1, -30]])

dst_image = cv2.warpAffine(image, M, (width, height))

# show_with_matplotlib(dst_image, 'Negative Warp Affine')

# Rotation

M = cv2.getRotationMatrix2D((width/2, height/2), 180, 1)

dst_image = cv2.warpAffine(image, M, (width, height))

# show_with_matplotlib(dst_image, "Rotation with matrix")

# Now, we are going to rotate the image 30 degrees changing the center of rotation
M = cv2.getRotationMatrix2D((width/1.5, height/1.5), 30, 1)
dst_image = cv2.warpAffine(image, M, (width, height))

# show_with_matplotlib(dst_image, "Rotation 30 degrees")

image_point = image.copy()
cv2.circle(image_point, (135, 45), 5, (255, 0, 255), -1)
cv2.circle(image_point, (385, 45), 5, (255, 0, 255), -1)
cv2.circle(image_point, (135, 230), 5, (255, 0, 255), -1)

# print(image_point.shape)

# show_with_matplotlib(image_point, "before Affine Transformation")

pts_1 = np.float32([[135, 45],
                    [385, 45],
                    [135, 230]])
pts_2 = np.float32([[135, 45], [385, 45], [180, 230]])

M = cv2.getAffineTransform(pts_1, pts_2)
dst_image = cv2.warpAffine(image_point, M, (width, height))

# show_with_matplotlib(dst_image, "Affine transformation")

image_points = image.copy()
cv2.circle(image_points, (450, 65), 5, (255, 0, 255), -1)
cv2.circle(image_points, (517, 65), 5, (255, 0, 255), -1)
cv2.circle(image_points, (431, 164), 5, (255, 0, 255), -1)
cv2.circle(image_points, (552, 164), 5, (255, 0, 255), -1)

# Show the image:
# show_with_matplotlib(image_points, 'before perspective transformation')

pts_1 = np.float32([[450, 65], [517, 65], [431, 164], [552, 164]])
pts_2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

M = cv2.getPerspectiveTransform(pts_1, pts_2)

dst_image = cv2.warpPerspective(image, M, (300, 300))

# show_with_matplotlib(dst_image, 'perspective_transformation')

# Cropping
# A copy of image is created to show the points that will be used for the cropping.
image_point = image.copy()

# Show the point and the line connecting the points:
cv2.circle(image_point, (230, 80), 5, (0, 0, 255), -1)
cv2.circle(image_point, (330, 80), 5, (0, 0, 255), -1)
cv2.circle(image_point, (230, 200), 5, (0, 0, 255), -1)
cv2.circle(image_point, (330, 200), 5, (0, 0, 255), -1)
cv2.line(image_point, (230, 80), (330, 80), (0, 0, 255))
cv2.line(image_point, (230, 80), (230, 200), (0, 0, 255))
cv2.line(image_point, (330, 80), (330, 200), (0, 0, 255))
cv2.line(image_point, (230, 200), (330, 200), (0, 0, 255))

show_with_matplotlib(image_point, 'Before Cropping')

dst_image = image[80:200, 230:330]

show_with_matplotlib(dst_image, 'After Cropping')
