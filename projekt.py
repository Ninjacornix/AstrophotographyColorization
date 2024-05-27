import argparse
from util.converter import convert_fits_to_tiff
from util.balancer import color_balance, denoise_image, infrared_balance
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

def main():
    r=fits.open("/Users/ninjacornix/DOAS/images/source/hlsp_heritage_hst_wfc3-uvis_m16_f673n_v1_drz.fits")[0].data
    g=fits.open("/Users/ninjacornix/DOAS/images/source/hlsp_heritage_hst_wfc3-uvis_m16_f657n_v1_drz.fits")[0].data
    b=fits.open("/Users/ninjacornix/DOAS/images/source/hlsp_heritage_hst_wfc3-uvis_m16_f502n_v1_drz.fits")[0].data

    r = np.nan_to_num(r)
    g = np.nan_to_num(g)
    b = np.nan_to_num(b)
    """ fig, ax = plt.subplots(1, 3, figsize=(15, 5))
    ax[0].imshow(r, cmap='gray', origin='lower')
    ax[0].set_title('673n')
    ax[1].imshow(g, cmap='gray', origin='lower')
    ax[1].set_title('657n')
    ax[2].imshow(b, cmap='gray', origin='lower')
    ax[2].set_title('502n')
    plt.show() """
    r, g, b = color_balance(r, g, b)
    rgb = np.dstack((r, g, b))
    plt.imshow(rgb, origin='lower')
    plt.show()
    rgb = denoise_image(rgb)
    plt.imshow(rgb, origin='lower')
    plt.show()

def infrared():
    a = fits.open("/Users/ninjacornix/DOAS/images/source/hlsp_heritage_hst_wfc3-ir_m16_f110w_v1_drz.fits")[0].data
    b = fits.open("/Users/ninjacornix/DOAS/images/source/hlsp_heritage_hst_wfc3-ir_m16_f160w_v1_drz.fits")[0].data

    a = np.nan_to_num(a)
    b = np.nan_to_num(b)

    a, b = infrared_balance(a, b)

    combined = np.dstack((a, np.zeros_like(a), b))
    plt.imshow(combined, origin='lower')
    plt.show()


if __name__ == "__main__":
    infrared()