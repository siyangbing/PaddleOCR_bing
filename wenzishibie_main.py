import os

yml_path = "configs/rec/rec_icdar15_train.yml"

trian_boxes_str = "python3 tools/train.py -c {0} 2>&1 | tee train_rec.log".format(yml_path)

if __name__ == "__main__":
    os.system(trian_boxes_str)
