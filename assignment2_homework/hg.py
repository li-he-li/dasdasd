from skimage import io
image = io.imread('x.jpg')
(h,w,c)=image.shape
print(h,w,c)
for i in range(1,9):
    for j in range(1,9):
        image[i, j, 1] = 255
        if image[i, j, 1] == 255:
            image[i, j, 2] = 0  
io.imshow(image)
io.show()