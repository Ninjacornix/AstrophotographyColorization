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

    ogshape = r.shape
    r = r.flatten()
    g = g.flatten()
    b = b.flatten()

    r = r.reshape(-1, 1)
    g = g.reshape(-1, 1)
    b = b.reshape(-1, 1)

    red_model = LinearRegression()
    red_model.fit(r, g)
    red = red_model.predict(r)
    red_model.fit(r, b)
    blue = red_model.predict(r)

    green_model = LinearRegression()
    green_model.fit(g, r)
    green = green_model.predict(g)
    green_model.fit(g, b)
    blue = green_model.predict(g)

    blue_model = LinearRegression()
    blue_model.fit(b, r)
    red = blue_model.predict(b)
    blue_model.fit(b, g)
    green = blue_model.predict(b)

    # reshape to original shape
    r = r.reshape(ogshape)
    g = g.reshape(ogshape)
    b = b.reshape(ogshape)

    lut_in = np.arange(256, dtype=np.uint8)
    lut_out = np.arange(256, dtype=np.uint8)

    lut_8u = np.interp(np.arange(256), lut_in, lut_out).astype(np.uint8)

    r = cv2.LUT(r, lut_8u)
    g = cv2.LUT(g, lut_8u)
    b = cv2.LUT(b, lut_8u)

    return r, g, b