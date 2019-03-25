import numpy as np
import math

def PSNR(img1, img2):
	MSE = np.mean( (img1/255. - img2/255.) ** 2 )
	if MSE == 0:
		return 1000
	R = 1
	return 20 * math.log10(R / math.sqrt(MSE))