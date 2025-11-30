import cv2
import numpy as np
import os

# Set the block size and magnification factor
bkS = 8
mag = 10

# Find the total number of patches (assuming they are saved in a folder named "dctPatches")
patch_folder = "dctPatches"
patches = [f for f in os.listdir(patch_folder) if f.endswith(".png")]

# Sort the patches based on their u, v coordinates (assumes filename format dctPatch_u_v.png)
patches.sort(key=lambda x: (int(x.split('_')[1]), int(x.split('_')[2].split('.')[0])))

# Calculate the size of the stitched image
num_patches_per_row = bkS  # as the patch grid is bkS x bkS
stitched_width = bkS * mag * num_patches_per_row
stitched_height = bkS * mag * num_patches_per_row

# Create a blank canvas to hold the stitched image
stitched_image = np.zeros((stitched_height, stitched_width), np.float32)

# Place each patch into the stitched image
for i, patch_name in enumerate(patches):
    # Calculate the row and column to place the patch in
    row = i // bkS
    col = i % bkS

    # Read the patch image
    patch_path = os.path.join(patch_folder, patch_name)
    patch = cv2.imread(patch_path, cv2.IMREAD_GRAYSCALE)

    # Calculate the position to place the patch
    y_offset = row * bkS * mag
    x_offset = col * bkS * mag

    # Place the patch into the stitched image
    stitched_image[y_offset:y_offset + bkS * mag, x_offset:x_offset + bkS * mag] = patch

# Normalize the stitched image to [0, 255] for visualization
stitched_image = cv2.normalize(stitched_image, None, 0, 255, cv2.NORM_MINMAX)
stitched_image = np.uint8(stitched_image)

# Save the stitched image
cv2.imwrite("stitched_dct_image.png", stitched_image)

print("Stitched image saved as 'stitched_dct_image.png'.")
