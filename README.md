## Summary

Both python files together generate and visualize the complete set of 64 two-dimensional DCT (Discrete Cosine Transform) basis functions used in an 8×8 JPEG compression block.

Each individual DCT basis pattern is computed by evaluating the cosine-frequency equations for every (u, v) pair and saving each result as a grayscale image patch.  Then all of these generated patches is loaded, sorted by their frequency indices, and stitched into a single large image that displays the entire DCT basis grid in one view.

Together, both scripts form a full pipeline that mathematically generates the DCT basis functions and assembles them into a comprehensive visualization of the frequency components used in JPEG image encoding.
