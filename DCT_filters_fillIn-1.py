import math
import cv2
import numpy as np

# blockSize
bkS = 8
# scale up blocks for easier visualization
mag = 10
    
for u in range(bkS):
    for v in range(bkS):
        # store computed DCT values in this variable
        image = np.zeros((bkS*mag, bkS*mag), np.float32)
        # update these values with the smallest and largest DCT value found for this block
        maxV = -100000.0
        minV = 100000.0
        
        #### fill in DCT calculation ####
        
        # Weights for scaling the DCT values
        alphaU = 0
        alphaV = 0

        # Give less weight to no variation in the horizontal
        if u == 0:
            alphaU = (1 / bkS) ** 0.5
        # Give more weight to variation in the horizontal
        else:
            alphaU = (2 / bkS) ** 0.5

        # Give less weight to no variation in the vertical
        if v == 0:
            alphaV = (1 / bkS) ** 0.5
        # Give more weight to variation in the vertical
        else:
            alphaV = (2 / bkS) ** 0.5

        # NOTE: x and y in the loop should technically be swapped.
        # I'm doing this so the 
        # the image that stitches all the DCT patches together will show 
        # x variation across rows and y variation across columns.

        # Looping over each pixel in the block
        for x in range(bkS):
            for y in range(bkS):
                # Calculate DCT values, applying weights to the frequency components u and v
                value = alphaU * alphaV * math.cos((((2*x)+1)*u*math.pi)/(2*bkS)) * math.cos((((2*y)+1)*v*math.pi)/(2*bkS))
                image[x][y] = value     # Temp variable for determining new max and min values

                # Tracking the largest and smallest DCT values in the block
                if value > maxV:
                    maxV = value
                if value < minV:
                    minV = value

        print("New largest DCT value: ", maxV)
        print("New smallest DCT value: ", minV)

        # DCT values need to be mapped to [0-255] for visualization        
        imageN = np.zeros((bkS*mag, bkS*mag), np.float32)
        if maxV == minV:    # No variation
            for x in range(bkS*mag):
                for y in range(bkS*mag):
                    imageN[y][x] = 255.0
        else:
            for x in range(bkS):    
                for m in range(mag):
                    for y in range(bkS):
                        val = 255.0*(image[y][x]-minV)/(maxV-minV)  
                        for n in range(mag):
                            imageN[mag*y+n][mag*x+m] = val
                            

        name = "dctPatches/dctPatch_" + str(u) + "_" + str(v) + ".png"
        cv2.imwrite(name, imageN)


