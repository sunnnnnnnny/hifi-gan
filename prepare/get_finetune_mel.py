import os
import shutil
from glob import glob

out_dir = "result_sub"
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

thresh_step = 1000

input_path_list = glob("./result/*npy")
for input_path in input_path_list:
    filename = input_path.split("/")[-1]
    filename_prefix = filename.split(".")[0]
    step = filename_prefix.split("_")[1]
    if int(step) < thresh_step:
        shutil.copyfile(input_path, os.path.join(out_dir, filename))


