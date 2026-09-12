#This script slices the image into a grid of blocks and shuffles them based on your Logistic Map key

import cv2
import numpy as np
import matplotlib.pyplot as plt

def generate_chaotic_key(x0, r, size):
    key = np.zeros(size)#array of zeroes
    x=x0
    for i in range(size):
        x=r*x*(1-x)#Each iteration uses the previous output as the next input:
        key[i]=x
    return key

img = cv2.imread('data/image.jpg', cv2.IMREAD_GRAYSCALE)
# 1. Load image and set block size (B x B)
B=16# Standard block size for learnable encryption

h,w = (img.shape[0]//B)*B, (img.shape[1]//B)*B
img=cv2.resize(img, (w,h))

# 2. Divide image into non-overlapping blocks
num_blocks_h, num_blocks_w = h// B, w//B
total_blocks = num_blocks_h* num_blocks_w

blocks=[]
for i in range(num_blocks_h):
    for j in range(num_blocks_w):
        blocks.append(img[i*B:(i+1)*B, j*B:(j+1)*B])
blocks=np.array(blocks)

key = generate_chaotic_key(x0=0.3541, r=3.999, size=total_blocks)
perm_order = np.argsort(key)
shuffled_blocks = blocks[perm_order]

# 4. Reconstruct cipher image
encrypted_img = np.zeros_like(img)
idx = 0
for i in range(num_blocks_h):
    for j in range(num_blocks_w):
        encrypted_img[i*B:(i+1)*B, j*B:(j+1)*B] = shuffled_blocks[idx]
        idx += 1

plt.subplot(1, 2, 1), plt.title("Original"), plt.imshow(img, cmap='gray')
plt.subplot(1, 2, 2), plt.title(f"Block Encrypted ({B}x{B})"), plt.imshow(encrypted_img, cmap='gray')
plt.show()


