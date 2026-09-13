import numpy as np
import day3_intra_block

def horizontal_correlation(image):
    # Extract adjacent pixel pairs (x and y)
    x = image[:, :-1].flatten()
    y = image[:, 1:].flatten()
    # Calculate Pearson correlation coefficient
    correlation_matrix = np.corrcoef(x, y)
    return correlation_matrix[0, 1]

def calculate_npcr_uaci(cipher1, cipher2):
    # Calculate NPCR
    diff_pixels = (cipher1 != cipher2).astype(int)
    npcr = np.mean(diff_pixels) * 100

    # Calculate UACI
    abs_diff = np.abs(cipher1.astype(float) - cipher2.astype(float))
    uaci = (np.mean(abs_diff) / 255.0) * 100
    return npcr, uaci

plain_corr = horizontal_correlation(day3_intra_block.img)
cipher_corr = horizontal_correlation(day3_intra_block.encrypted_img)

print(f"Plaintext Correlation: {plain_corr:.4f}")
print(f"Ciphertext Correlation: {cipher_corr:.4f}")

# Simulate a differential attack (change 1 pixel in original image and re-encrypt)
img_altered = day3_intra_block.img.copy()
img_altered[0, 0] = (img_altered[0, 0] + 1) % 256