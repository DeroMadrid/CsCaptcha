import os
import random
import shutil

image_path = "D:/Lab_work_XCX/DATASET/VTT/cs/"
output_path = "C:/Users/hikari/Desktop/data/"
csv_file = "C:/Users/hikari/Desktop/val_rs_2w.csv"

with open(csv_file) as file:
    for line in file:
        img_name = line.split(',')[0]
        if img_name != "filename":
            cls_name = ""
            for i in range(len(img_name)):
                if img_name[i].isdigit():
                    break
                else:
                    cls_name = cls_name + img_name[i]
            img_id = "".join(list(filter(str.isdigit,  img_name)))

            filee_list = os.listdir(image_path+cls_name)
            for filee in filee_list:
                idd = "".join(list(filter(str.isdigit,  filee)))
                if idd == img_id:
                    old_path = image_path+cls_name+'/'+filee
                    new_path = output_path + cls_name + idd +'.jpg'
                    print(new_path)
                    shutil.copyfile(old_path, new_path)



