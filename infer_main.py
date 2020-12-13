import os

yml_path = "configs/rec/rec_icdar15_train.yml"
checkpoints_path = "./output/rec_CRNN/best_accuracy"
img_path = "./train_data/ic15_data/test/word_38.png"

trian_boxes_str = "python tools/infer_rec.py -c {0} -o Global.checkpoints={1} Global.infer_img={2}".format(
    yml_path,checkpoints_path,img_path)

if __name__ == "__main__":
    os.system(trian_boxes_str)
