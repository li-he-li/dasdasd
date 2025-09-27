from skimage import io
image = io.imread('x.jpg')
(h,w,c)=image.shape
print(h,w,c)
for i in range(3,7):
    for j in range(3,7):
        image[i, j, 0] = 255
io.imshow(image)
io.show()