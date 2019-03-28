import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
from scipy import signal
from scipy import misc
from generate_PSF import PSF
from generate_trajectory import Trajectory
from blur_image import BlurImage

def fix_point():
    point = None

    return point



if __name__ == '__main__':
    folder = 'raw_images'
    folder_to_save = 'blurred_images'
    params = [0.01, 0.009, 0.008, 0.007, 0.005, 0.003]
    for path in os.listdir(folder):
        if path.startswith('.'):
            continue
        print(path)
        trajectory = Trajectory(canvas=64, max_len=60, expl=np.random.choice(params)).fit()
        psf = PSF(canvas=64, trajectory=trajectory).fit()
        BlurImage(os.path.join(folder, path), PSFs=psf,
                    path__to_save=folder_to_save, part=np.random.choice([1, 2, 3])).blur_image(show=True)

