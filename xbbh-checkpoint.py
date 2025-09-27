from skimage import io
image = io.imread('x.jpg')
(h,w,c)=image.shape
print(h,w,c)
for i in range(w//2):
        image[:, i, 0] = 255

# 显示处理后的图像
io.imshow(image)
io.show()