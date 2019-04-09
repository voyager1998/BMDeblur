from PIL import Image
import os, sys
import matplotlib.pyplot as plt
from skimage import data, color
from skimage.transform import rescale, downscale_local_mean

def down(path, sub):
    dirs = os.listdir(path + sub)
    for item in dirs:
        if os.path.isfile(path + sub + item):
            im = Image.open(path + sub + item)
            f, _ = os.path.splitext(path + sub + item)
            width, height = im.size
            imResize = im.resize((int(width / 2), int(height / 2)), Image.ANTIALIAS)
            imResize.save(f + '.png', 'png')

subdir = ["test/", "train/", "val/"]
path = "~/Downloads/442_proj/pytorch-CycleGAN-and-pix2pix/datasets/GOPRO_for_comb/A/"
for sub in subdir:
    down(path, sub)

path = "~/Downloads/442_proj/pytorch-CycleGAN-and-pix2pix/datasets/GOPRO_for_comb/B/"
for sub in subdir:
    dirs = os.listdir(path + sub)
    down(path, sub)
    
