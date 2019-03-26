import os
from options.test_options import TestOptions
from data import create_dataset
from models import create_model
from util.visualizer import save_images
from util import html
from util import metrics
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    opt = TestOptions().parse()  # get test options
    # hard-code some parameters for test
    opt.num_threads = 0   # test code only supports num_threads = 1
    opt.batch_size = 1    # test code only supports batch_size = 1
    opt.serial_batches = True  # disable data shuffling; comment this line if results on randomly chosen images are needed.
    opt.no_flip = True    # no flip; comment this line if results on flipped images are needed.
    opt.display_id = -1   # no visdom display; the test code saves the results to a HTML file.
    dataset = create_dataset(opt)  # create a dataset given opt.dataset_mode and other options

    step = 100
    final_epoch = 200
    all_epochs = []
    all_PSNR = []
    
    for n_epoch in range(step, final_epoch + 1, step):
        opt.epoch = n_epoch
        model = create_model(opt)      # create a model given opt.model and other options
        model.setup(opt)  # regular setup: load and print networks; create schedulers
        
        # test with eval mode. This only affects layers like batchnorm and dropout.
        # For [pix2pix]: we use batchnorm and dropout in the original pix2pix. You can experiment it with and without eval() mode.
        # For [CycleGAN]: It should not affect CycleGAN as CycleGAN uses instancenorm without dropout.
        if opt.eval:
            model.eval()

        counter = 0
        avgPSNR = 0.0
        
        for i, data in enumerate(dataset):
            if i >= opt.num_test:  # only apply our model to opt.num_test images.
                break
            counter = i
            model.set_input(data)  # unpack data from data loader
            model.test()           # run inference
            visuals = model.get_current_visuals()  # get image results
            avgPSNR += metrics.cal_PSNR(visuals['fake_B'], visuals['real_B'])
        avgPSNR = avgPSNR / (counter + 1)
        print("Epoch ", n_epoch, "  Average PSNR = ", avgPSNR)
        all_epochs += [n_epoch]
        all_PSNR += [avgPSNR]
    
    # Plot PSNR vs epoch
    plt.plot(all_epochs, all_PSNR, 'r-')
    plt.axis([0, final_epoch + step, 15, 30])
    plt.savefig('results/PSNR_vs_epoch.png')

    all_PSNR = np.array(all_epochs)
    print("Epoch with highest validation PSNR: ", np.argmax(all_epochs) * step)
    