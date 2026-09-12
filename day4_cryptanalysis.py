import day3_intra_block
import math
import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_entropy(image):
    #pixel histogram
    hist, _ = np.histogram(image.flatten(), bins=256, range=[0,256])
    prob_density = hist/hist.sum()

    #Calculate Shannon Entropy
    entropy = -np.sum([p * math.log2(p) for p in prob_density if p > 0])
    return entropy
#calculate entropies
plain_entropy = calculate_entropy(day3_intra_block.img)
cipher_entropy = calculate_entropy(day3_intra_block.encrypted_img)

print(f"Plaintext Entropy: {plain_entropy:.4f}")
print(f"Ciphertext Entropy: {cipher_entropy:.4f}")

# 2. Plot Histograms
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.title("Plaintext Histogram")
plt.hist(day3_intra_block.img.flatten(), bins=256, color='blue', alpha=0.7)

plt.subplot(1, 2, 2)
plt.title("Ciphertext Histogram")
plt.hist(day3_intra_block.encrypted_img.flatten(), bins=256, color='red', alpha=0.7)
plt.show()