from util.converter import convert_fits_to_tiff
from util.balancer import color_balance, denoise_image, color_curve, lower_brightness_increase_vibrancy
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

def uvis():
    r=fits.open("images/source/hlsp_heritage_hst_wfc3-uvis_m16_f673n_v1_drz.fits")[0].data # 673n high
    g=fits.open("images/source/hlsp_heritage_hst_wfc3-uvis_m16_f657n_v1_drz.fits")[0].data # 657n low
    b=fits.open("images/source/hlsp_heritage_hst_wfc3-uvis_m16_f502n_v1_drz.fits")[0].data # 502n 

    r = np.nan_to_num(r)
    g = np.nan_to_num(g)
    b = np.nan_to_num(b)
    
    r, g, b = color_balance(r, g, b)
    r, g, b = color_curve(r, g, b)
    rgb = np.dstack((r, g, b))
    
    rgb = denoise_image(rgb)
    rgb = lower_brightness_increase_vibrancy(rgb)
    plt.imshow(rgb, origin='lower')
    plt.title('M16 UVIS denoised')
    plt.show()

def infrared():
    blue = fits.open("images/source/hlsp_heritage_hst_wfc3-ir_m16_f110w_v1_drz.fits")[0].data
    yellow = fits.open("images/source/hlsp_heritage_hst_wfc3-ir_m16_f160w_v1_drz.fits")[0].data

    blue = np.nan_to_num(blue)
    yellow = np.nan_to_num(yellow)

    red = yellow * 0.3
    green = yellow * 0.7
    
    red, green, blue = color_balance(red, green, blue)
    red, green, blue = color_curve(red, green, blue)

    infrared = np.dstack((red, green, blue))
    infrared = denoise_image(infrared)
    infrared = lower_brightness_increase_vibrancy(infrared)

    plt.imshow(infrared, origin='lower')
    plt.title('IR')
    plt.show()


if __name__ == "__main__":
    uvis()
    infrared()