import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import make_lupton_rgb

def colorise_image(r, g, b):
    forc = np.float_()
    r = np.array(r, forc) * 0.5
    g = np.array(g, forc) * 0.1
    b = np.array(b, forc) * 0.5

    rgb_default = make_lupton_rgb(r,g,b,Q=1,stretch=0.1,filename="pillar.png")
    plt.imshow(rgb_default, origin='lower')
    print("Showing image")
    plt.show()
