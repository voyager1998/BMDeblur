rm ./GOPRO_for_comb/*/*/*
cp ./GOPRO_Large/train/*/sharp/* ./GOPRO_for_comb/A/train
cp ./GOPRO_Large/train/*/blur/* ./GOPRO_for_comb/B/train
cp ./GOPRO_Large/test/*/sharp/* ./GOPRO_for_comb/A/test
cp ./GOPRO_Large/test/*/blur/* ./GOPRO_for_comb/B/test
cp ./GOPRO_Large/test/*/sharp/* ./GOPRO_for_comb/A/val
cp ./GOPRO_Large/test/*/blur/* ./GOPRO_for_comb/B/val

# for d in ./GOPRO_Large/train/*/ ;
# do (cd "$d" && cd blur_gamma/ && bash ~/Downloads/rename_gamma.sh &&
#     cd ../sharp/ && bash ~/Downloads/rename_gamma.sh);
# done
# cp ./GOPRO_Large/train/*/sharp/* ./GOPRO_for_comb/A/train
# cp ./GOPRO_Large/train/*/blur_gamma/* ./GOPRO_for_comb/B/train


# for d in ./GOPRO_Large/train/*/ ;
# do (cd "$d" && cd blur_gamma/ && bash ~/Downloads/rename_back.sh &&
#     cd ../sharp/ && bash ~/Downloads/rename_back.sh);
# done

for d in ./GOPRO_Large/train/*/ ;
do (cd "$d" && cd blur_gamma/ && bash ~/Downloads/442_proj/pytorch-CycleGAN-and-pix2pix/datasets/rename_gamma.sh &&
    cd ../sharp/ && bash ~/Downloads/442_proj/pytorch-CycleGAN-and-pix2pix/datasets/rename_gamma.sh);
done
cp ./GOPRO_Large/train/*/sharp/* ./GOPRO_for_comb/A/train
cp ./GOPRO_Large/train/*/blur_gamma/* ./GOPRO_for_comb/B/train


for d in ./GOPRO_Large/train/*/ ;
do (cd "$d" && cd blur_gamma/ && bash ~/Downloads/442_proj/pytorch-CycleGAN-and-pix2pix/datasets/rename_back.sh &&
    cd ../sharp/ && bash ~/Downloads/442_proj/pytorch-CycleGAN-and-pix2pix/datasets/rename_back.sh);
done

cd ~/Downloads/442_proj/pytorch-CycleGAN-and-pix2pix/datasets/
python3 downscale.py