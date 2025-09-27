from skimage import io
image = io.imread('x.jpg')
(h,w,c)=image.shape
print(h,w,c)
for i in range(h//2):
    for j in range(w//2):
        image[i, j, 0] = 255
io.imshow(image)
io.show()