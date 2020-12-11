import os


yml_path = "configs/det/det_mv3_db_v1.1.yml"



trian_boxes_str = "python3 tools/train.py -c {0} -o Optimizer.base_lr=0.0001 ".format(yml_path)


if __name__=="__main__":
    os.system(trian_boxes_str)