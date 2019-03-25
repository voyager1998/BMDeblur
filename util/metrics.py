import numpy as np
import math
# import tensorflow as tf
import torch

def cal_PSNR(img1, img2):
    img1 = img1.numpy()
    img1 = img1.astype(float)
    
    img2 = img2.numpy()
    img2 = img2.astype(float)
    
    # Validate R = 2:
    # print("MAX = ",np.amax(img1))
    # print("MIN = ",np.amin(img1))
    # print("MAX = ",np.amax(img2))
    # print("MIN = ",np.amin(img2))

    # img1 = np.mean(img1, axis=(0, 1))
    # img2 = np.mean(img2, axis=(0, 1))    
    # print("image size: ",img1.shape)
    result = 100

    # se = 0.0
    # for i in range(len(img1)):
    #     for j in range(len(img1[0])):
    #         se += (img1[i][j] - img2[i][j] ) ** 2
    # my_mse = se / (len(img1) * len(img1[0]))
    mse = np.mean((img1  - img2 ) ** 2)
    # print("MSE, my_MSE = ", mse,my_mse)

    # print("MSE size = ",mse.shape)
    if mse != 0:
        R = 2   #TODO: what is R exactly? Look into the format of visuals = model.get_current_visuals()
        result = 20 * math.log10(R / math.sqrt(mse))
    return result