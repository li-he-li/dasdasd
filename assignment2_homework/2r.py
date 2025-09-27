from skimage import io
image = io.imread('galaxy-full.jpg')
(h,w,c)=image.shape
print(h,w,c)
for i in range(533):
    for j in range(525):
            image[i, j, 1] =0
            image[i, j, 2] =0 
 
io.imshow(image)
io.show()

from skimage import io
image = io.imread('galaxy-full.jpg')
(h,w,c)=image.shape
print(h,w,c)
for i in range(533):
    for j in range(525):
            image[i, j, 0] =0
            image[i, j, 2] =0 
 
io.imshow(image)
io.show()

from skimage import io
image = io.imread('galaxy-full.jpg')
(h,w,c)=image.shape
print(h,w,c)
for i in range(533):
    for j in range(525):
            image[i, j, 0] =0
            image[i, j, 1] =0 
 
io.imshow(image)
io.show()