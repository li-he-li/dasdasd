from skimage import io
import numpy as np
image = io.imread('earth.jpg')
(h,w,c)=image.shape
print(h,w,c)
for i in range(w):
    # 随机选择要设置的通道（0:红，1:绿，2:蓝）
    channel = np.random.randint(0, 3)
    # 将随机选择的通道值设置为255
    image[:, i, channel] = 255
io.imshow(image)
io.show()