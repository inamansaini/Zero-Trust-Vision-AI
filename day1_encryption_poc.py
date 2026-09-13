#Day 1(7/09/2026)

import cv2 
import numpy as np
import matplotlib.pyplot as plt
import logs

def generate_chaotic_key(x0, r, size):
    #function with 3 inputs
    key=np.zeros(size)
    x=x0
    for i in range (size):
        x=r*x*(1-x)#formula of logistic map Xn+1 = r*Xn(1-Xn)
        key[i]=x
    return key

#load image
img = cv2.imread('data/image.jpg', cv2.IMREAD_GRAYSCALE)
h, w=img.shape
flat_img=img.flatten()

# 2. Generate chaotic key (x0 and r are your secret keys)
# r must be between 3.56995 and 4 for chaotic behavior
key = generate_chaotic_key(x0=0.12345, r= 3.998, size=h*w)
# 3. Create a permutation map from the chaotic sequence
permutation_indices=np.argsort(key)
# 4. Scramble the image
encrypted_flat = flat_img[permutation_indices]
encrypted_img = encrypted_flat.reshape(h, w)
# 5. Visualize Plaintext vs Ciphertext

plt.subplot(1,2,1), plt.title('Original'), plt.imshow(img, cmap='gray')
plt.subplot(1, 2, 2), plt.title("Encrypted"), plt.imshow(encrypted_img, cmap='gray')
plt.show()

    