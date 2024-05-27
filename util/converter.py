import glob
import numpy as np
from astropy.io import fits
import imageio
import matplotlib.pyplot as plt

def convert_fits_to_tiff(fits_dir, tiff_dir):
    fits_files = glob.glob(fits_dir + '/*.fits')
    for fits_file in fits_files:
        hdul = fits.open(fits_file)
        data = hdul[0].data
        data = np.clip(data, 0, 255)
        data = data.astype(np.uint8)
        tiff_file = tiff_dir + '/' + fits_file.split('/')[-1].replace('.fits', '.tiff')
        imageio.imwrite(tiff_file, data)
        hdul.close()



    
def convert_single_fits_to_tiff(fits_file, tiff_file):
    hdul = fits.open(fits_file)
    data = hdul[0].data
    data = np.clip(data, 0, 255)
    data = data.astype(np.uint8)
    imageio.imwrite(tiff_file, data)
    hdul.close()