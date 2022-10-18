import os
import random
import shutil
import cls_dict
import csv
from PIL import Image

"""
add new label to dict
"""
def add_new_label():
    dic_a = str(cls_dict.cls)
    new_dict = {}
    class_star_num = 1000
    img_path = "/home/abc/xcx/vtt/data/security_test/img2/"
    tmp_file = "tmp.txt"
    imgs = os.listdir(img_path)
    num = 0
    """for image file"""
    for img in imgs:
        num += 1
        label = ""
        for i in range(len(img)):
            if img[i].isdigit():
                break
            else:
                label = label + img[i]

        print(str(num) +  "-----"+ str(class_star_num))
        if label not in dic_a:
            if label not in str(new_dict):
                new_dict[str(class_star_num)] = label
                f = open(tmp_file, "a")
                context = " " + str(class_star_num) + ": '" + label + "',\n"
                f.write(context)
                class_star_num += 1

"""
Generating csv file
"""
def create_csv():
    file_path = "/home/abc/xcx/vtt/data/security_test/img2/"
    files = os.listdir(file_path)

    header = ['filename', 'label']
    num = 0
    with open('val_rs2.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)
        # write the data
        for filee in files:
            num += 1
            print(num)
            filename = filee
            cls = ""
            for t in range(len(filee)):
                if filee[t].isdigit():
                    break
                else:
                    cls += filee[t]

            for t in range(len(cls_dict.cls)):
                if cls in cls_dict.cls[t]:
                    label = str(t + 1)
                    if int(label) > 1000:
                        label = int(label) - 1000
                    break

            data = [filename, label]
            writer.writerow(data)



"""
change file name
"""
def change_name():
    old_path = "D:/Lab_work_XCX/A-VTT/experiment/imgProcess/afterpro_data/"
    new_path = "D:/Lab_work_XCX/A-VTT/experiment/imgProcess/data/"

    clss = os.listdir(old_path)
    for cls in clss:
        cls_path = old_path + cls
        files = os.listdir(cls_path)
        for file in files:
            id = "".join(filter(str.isdigit, file))
            new_name = cls + id + '.jpg'
            old_file = cls_path + '/' + file
            new_file = new_path + new_name
            shutil.copyfile(old_file, new_file)
        print(cls)

"""
Delete images that cannot be opened
"""
def delete_errorimg():
    img_path = "/home/abc/xcx/vtt/SI-NI-FGSM-master/dev_data/val_rs/"
    files = os.listdir(img_path)
    i = 0
    for file in files:
        imgp = img_path + file
        img = cv2.imread(imgp, 1)
        try:
            if img.any() == None:
                print(img_path)
        except:
            i += 1
            print(imgp)
            os.remove(imgp)
    print(i)


"""
Generating csv file for RGB image
"""
def create_csv_rgb():
    imgs = os.listdir("/home/abc/xcx/vtt/SI-NI-FGSM-master/dev_data/val_rs/")
    img_num = 0
    header = ['filename', 'label']

    with open('/home/abc/xcx/vtt/SI-NI-FGSM-master/dev_data/val_rs_2w.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)
        # write the data
        for img in imgs:
            img_num += 1
            if img_num == 20000:
                break
            else:
                label = ""
                for k in range(len(img)):
                    if img[k].isdigit():
                        break
                    else:
                        label = label + img[k]

                for t in range(1000):
                    if label in cls_dict.cls[t]:
                        id = str(t + 1)
                        break
                data = [img, id]
                writer.writerow(data)

"""
Extract image from cvs file
"""
def extract_img():
    img_pa = os.listdir("/home/abc/xcx/vtt/SI-NI-FGSM-master/dev_data/val_rs/")

    with open('/home/abc/xcx/vtt/SI-NI-FGSM-master/dev_data/val_rs_2w.csv') as file:
        for line in file:
            img_name = line.split(',')[0]
            if not img_name == "filename":
                img_oldpath = "/home/abc/xcx/vtt/SI-NI-FGSM-master/dev_data/val_rs/" + img_name
                img_newpath = "/home/abc/xcx/vtt/SI-NI-FGSM-master/dev_data/val_rs_2w/" + img_name
                shutil.copyfile(img_oldpath, img_newpath)

"""
Change img format
"""
def change_format():
    files = os.listdir("/home/abc/xcx/vtt/SI-NI-FGSM-master/clean_data/data/")
    for file in files:
        old_name = "/home/abc/xcx/vtt/SI-NI-FGSM-master/clean_data/data/"+file
        new_name = "/home/abc/xcx/vtt/SI-NI-FGSM-master/clean_data/data/" + file.split('.')[0]+'.JPEG'
        os.rename(old_name, new_name)

"""
Save files in separate folders
"""
def sav_files():
    files = "/home/abc/xcx/vtt/data/adv_data/"
    filess = os.listdir(files)
    train_file = "/home/abc/xcx/vtt/data/adv_train/"
    test_file = "/home/abc/xcx/vtt/data/adv_test/"
    num = 0
    for file in filess:
        if num < 20000:
            file_cls = ""
            for i in range(len(file)):
                if not file[i].isdigit():
                    file_cls = file_cls + file[i]
                else:
                    break
            cls_path = train_file + file_cls
            if not os.path.exists(cls_path):
                os.mkdir(cls_path)
                print(cls_path)

            old_path = files + file
            new_path = cls_path + '/' + file
            shutil.copyfile(old_path,new_path)

        else:
            old_path = files + file
            new_path = test_file + file
            shutil.copyfile(old_path, new_path)

        num += 1
        print(num)

"""
png trans to jpg
"""
def png_to_jpg():
    clss_path = "/home/abc/xcx/vtt/classify/inceptionV3/retrain/data/train/"
    clss = os.listdir(clss_path)
    num = 0
    for cls in clss:
        files = clss_path + cls + '/'
        filee = os.listdir(files)
        for file in filee:
            if file.split('.')[1] == 'png':
                os.remove(files+file)
            new_name = file.split('.')[0]+'.jpg'
            im = Image.open(files+file)
            im = im.convert('RGB')
            im.save(files+new_name)
            print(files+new_name)

add_new_label()
# create_csv()
