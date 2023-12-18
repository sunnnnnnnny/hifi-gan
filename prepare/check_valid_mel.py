import os
from glob import glob


names_set = set()
input_dir = "/Users/zhangsan/PycharmProjects/finetune_fs2/dongdie_record_first_mel_finetune"
mel_path_list = glob(input_dir + "/*npy")

print(len(mel_path_list))
for mel_path in mel_path_list:
    filename = mel_path.split("/")[-1]
    name = filename.split(".")[0].split("_")[-1]
    names_set.add(name)

print(names_set)
print(len(names_set))
names_list = list(names_set)
names_list.sort()
train_names = names_list[:-10]
val_names = names_list[-10:]
with open("../interal-data/training.txt", "w") as log:
    for name in train_names:
        line = name + "|" + "nothing" + "\n"
        log.write(line)
with open("../interal-data/validation.txt", "w") as log:
    for name in val_names:
        line = name + "|" + "nothing" + "\n"
        log.write(line)
