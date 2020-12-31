import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure

# ############################## 1.
src = cv2.imread("me.jpg")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))

# # 画像を読み込む。
# src = cv2.imread('me.jpg')
# gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3));
# opening = cv2.morphologyEx(
#     binary, cv2.MORPH_OPEN, kernel, iterations=2)
# ret, contours, hierarchy = cv2.findContours(
#     opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# drawn = cv2.drawContours(src.copy(), contours, -1, (0, 255, 0), 2)
# plt.imshow(drawn, cmap=plt.cm.gray)
# #plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
# plt.show()

# ## 2.
img = cv2.imread("me.jpg")
edges = cv2.Canny(img, 100, 200)
contours = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[1]


# Find contours at a constant value of 0.8
contours = measure.find_contours(r, 0.8)

# Display the image and plot all contours found
fig, ax = plt.subplots()
ax.imshow(r, interpolation="nearest", cmap=plt.cm.gray)

for n, contour in enumerate(contours):
    ax.plot(contour[:, 1], contour[:, 0], linewidth=2)


# 2値化(retvalに使用した閾値が、binary_imageに2値化した画像が入る)
# この場合はthreshholdを指定しているのでretvalに同じ値が入るが、
# cv2.THRESH_OTSU(大津の二値化)等の自動でthreshholdを算出する場合にretvalの値を使う。
threshhold = 150
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval, binary_image = cv2.threshold(img, threshhold, 255, cv2.THRESH_BINARY)
plt.imshow(binary_image, cmap=plt.cm.gray)

# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
cnt = np.squeeze(contours, axis=1)


def draw_contours(ax, img, contours):
    ax.imshow(img)
    for i, cnt in enumerate(contours):
        cnt = np.squeeze(cnt, axis=1)  # (NumPoints, 1, 2) -> (NumPoints, 2)
        ax.add_patch(Polygon(cnt, color="b", fill=None, lw=2))
        ax.plot(cnt[:, 0], cnt[:, 1], "ro", mew=0, ms=4)


fig, ax = plt.subplots(figsize=(6, 6))
draw_contours(ax, img, contours)
plt.show()


img = cv2.imread("me.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
_, contours, hierarchy = cv2.findContours(thresh, 2, 1)
cnt = contours[0]

hull = cv2.convexHull(cnt, returnPoints=False)


# contours, _ = cv2.findContours(...) # Your call to find the contours using OpenCV 2.4.x
# _, contours, _ = cv2.findContours(...) # Your call to find the contours
idx = -1  # The index of the contour that surrounds your object
mask = np.zeros_like(img)  # Create mask where white is what we want, black otherwise
cv2.drawContours(mask, contours, idx, 255, -1)  # Draw filled contour in mask
out = np.zeros_like(img)  # Extract out the object and place into output image
out[mask == 255] = img[mask == 255]

# Now crop
(y, x) = np.where(mask == 255)
(topy, topx) = (np.min(y), np.min(x))
(bottomy, bottomx) = (np.max(y), np.max(x))
out = out[topy : bottomy + 1, topx : bottomx + 1]
# plt.imshow(out)
# plt.show()
# Show the output image
# cv2.imshow('Output', out)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
