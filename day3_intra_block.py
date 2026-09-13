import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
import os
import logs

def generate_chaotic_key(x0, r, size):
    key = np.zeros(size)

    x=x0
    for i in range(size):
        x=r*x*(1-x)
        key[i]=x
    return key

img = cv2.imread(f"data/{random.choice(os.listdir('data'))}", 0)
B=128
h= (img.shape[0]//B)*B
w= (img.shape[1]//B)*B

img=cv2.resize(img, (w,h))

num_blocks_h= h//B
num_blocks_w=w//B

total_blocks = num_blocks_h * num_blocks_w

# Extract blocks
blocks=[]
for i in range(num_blocks_h):
    for j in range(num_blocks_w):
        blocks.append(img[i*B:(i+1)*B, j*B:(j+1)*B])
blocks=np.array(blocks)
blocks = np.array(blocks)

#Generate three chaotic keys

key_shuffle = generate_chaotic_key(0.123, 3.999, total_blocks)
key_rotate = (generate_chaotic_key(0.456, 3.999, total_blocks) * 4).astype(int) # Values: 0, 1, 2, 3
key_invert = (generate_chaotic_key(0.789, 3.999, total_blocks) * 2).astype(int) # Values: 0, 1

#Apply Intra-Block Transformations

transformed_blocks=[]
for i in range (total_blocks):
    blk=blocks[i]

    blk=np.rot90(blk, k=key_rotate[i]) #rotate 90
    #invert
    if key_invert[i]==1:
        blk=255-blk
    transformed_blocks.append(blk)

    #Shuffle and Reconstruct
transformed_blocks = np.array(transformed_blocks)
perm_order = np.argsort(key_shuffle)
shuffled_blocks = transformed_blocks[perm_order]

encrypted_img = np.zeros_like(img)
idx = 0
for i in range(num_blocks_h):
    for j in range(num_blocks_w):
        encrypted_img[i*B:(i+1)*B, j*B:(j+1)*B] = shuffled_blocks[idx]
        idx += 1

plt.subplot(1, 2, 1), plt.title("Original"), plt.imshow(img, cmap='gray')
plt.subplot(1, 2, 2), plt.title("Hardened Cipher"), plt.imshow(encrypted_img, cmap='gray')
plt.show()
