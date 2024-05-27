import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import cv2

def denoise_image(image):
    return cv2.fastNlMeansDenoising(image, None, 10, 7, 21)



def color_balance(r, g, b):
    r_ratio = 255 / np.percentile(r, 99)
    g_ratio = 255 / np.percentile(g, 99)
    b_ratio = 255 / np.percentile(b, 99)

    r = np.clip(r * r_ratio, 0, 255).astype(np.uint8)
    g = np.clip(g * g_ratio, 0, 255).astype(np.uint8)
    b = np.clip(b * b_ratio, 0, 255).astype(np.uint8)

    return r, g, b

def infrared_balance(a, b):
    a_ratio = 255 / np.percentile(a, 99)
    b_ratio = 255 / np.percentile(b, 99)

    a = np.clip(a * a_ratio, 0, 255).astype(np.uint8)
    b = np.clip(b * b_ratio, 0, 255).astype(np.uint8)

    return a, b