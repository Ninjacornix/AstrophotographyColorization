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

def color_curve(r, g, b):
    r = r.astype(np.float32)
    g = g.astype(np.float32)
    b = b.astype(np.float32)

    r_flat = r.flatten().reshape(-1, 1)
    g_flat = g.flatten().reshape(-1, 1)
    b_flat = b.flatten().reshape(-1, 1)

    red_model_g = LinearRegression()
    red_model_g.fit(r_flat, g_flat)
    red_g = red_model_g.predict(r_flat)

    red_model_b = LinearRegression()
    red_model_b.fit(r_flat, b_flat)
    red_b = red_model_b.predict(r_flat)

    green_model_r = LinearRegression()
    green_model_r.fit(g_flat, r_flat)
    green_r = green_model_r.predict(g_flat)

    green_model_b = LinearRegression()
    green_model_b.fit(g_flat, b_flat)
    green_b = green_model_b.predict(g_flat)

    blue_model_r = LinearRegression()
    blue_model_r.fit(b_flat, r_flat)
    blue_r = blue_model_r.predict(b_flat)

    blue_model_g = LinearRegression()
    blue_model_g.fit(b_flat, g_flat)
    blue_g = blue_model_g.predict(b_flat)

    r_new = (red_g + red_b) / 2
    g_new = (green_r + green_b) / 2
    b_new = (blue_r + blue_g) / 2

    r_new = r_new.reshape(r.shape)
    g_new = g_new.reshape(g.shape)
    b_new = b_new.reshape(b.shape)

    r_new = np.clip(r_new, 0, 255).astype(np.uint8)
    g_new = np.clip(g_new, 0, 255).astype(np.uint8)
    b_new = np.clip(b_new, 0, 255).astype(np.uint8)

    return r_new, g_new, b_new

def lower_brightness_increase_vibrancy(image, brightness_scale=1.1, saturation_scale=1.3):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    
    h, s, v = cv2.split(hsv_image)
    v = np.clip(v * brightness_scale, 0, 255).astype(np.uint8)
    s = np.clip(s * saturation_scale, 0, 255).astype(np.uint8)
    
    hsv_image = cv2.merge([h, s, v])
    enhanced_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2RGB)
    
    return enhanced_image
