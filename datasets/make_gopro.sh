cp ./GOPRO_Large/train/*/sharp/* ./GOPRO_data/A/train
cp ./GOPRO_Large/train/*/blur/* ./GOPRO_data/B/train
cp ./GOPRO_Large/test/*/sharp/* ./GOPRO_data/A/test
cp ./GOPRO_Large/test/*/blur/* ./GOPRO_data/B/test
cp ./GOPRO_Large/test/*/sharp/* ./GOPRO_data/A/val
cp ./GOPRO_Large/test/*/blur/* ./GOPRO_data/B/val


for d in ./GOPRO_Large/train/*/ ;
do (cd "$d" && cd blur_gamma/ && bash ~/Downloads/rename_gamma.sh &&
    cd ../sharp/ && bash ~/Downloads/rename_gamma.sh);
done
cp ./GOPRO_Large/train/*/sharp/* ./GOPRO_data/A/train
cp ./GOPRO_Large/train/*/blur_gamma/* ./GOPRO_data/B/train


for d in ./GOPRO_Large/train/*/ ;
do (cd "$d" && cd blur_gamma/ && bash ~/Downloads/rename_back.sh &&
    cd ../sharp/ && bash ~/Downloads/rename_back.sh);
done

