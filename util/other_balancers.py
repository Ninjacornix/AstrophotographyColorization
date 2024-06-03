

import cv2
import numpy as np

def gray_world(image):
    # Split the image into its BGR channels
    B, G, R = cv2.split(image)
    
    # Calculate the mean value for each channel
    B_mean = np.mean(B)
    G_mean = np.mean(G)
    R_mean = np.mean(R)
    
    # Calculate the overall mean of the B, G, R means
    overall_mean = (B_mean + G_mean + R_mean) / 3
    
    # Calculate scaling factors
    B_scale = overall_mean / B_mean
    G_scale = overall_mean / G_mean
    R_scale = overall_mean / R_mean
    
    # Apply scaling factors
    B = cv2.multiply(B, B_scale)
    G = cv2.multiply(G, G_scale)
    R = cv2.multiply(R, R_scale)
    
    # Merge the channels back together
    balanced_image = cv2.merge([B, G, R])
    
    return balanced_image

# Example usage
# Load the image
image_path = "D:/FER/Diplomski - FER/2. semestar/Digitalna obrada i analiza slike/Projekt/AstrophotographyColorization/util/img/nebula.png"
image = cv2.imread(image_path)

# Apply Gray World Assumption for color balancing
balanced_image = gray_world(image)

# Save the resulting image
cv2.imwrite('balanced_image.jpg', balanced_image)

# Display the original and balanced images
cv2.imshow('Original Image', image)
cv2.imshow('Balanced Image', balanced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()