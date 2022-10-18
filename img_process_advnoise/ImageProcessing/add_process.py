import processing
import os
import random
import cv2
import shutil

def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

def add_process_to_challenge(challenge_path, out_path):
    challenges = os.listdir(challenge_path)

    for challeng in challenges:
        print(challeng)
        images = os.listdir(challenge_path + challeng)

        for image in images:
            img_path = challenge_path + challeng + '/' + image
            try:
                img = processing.read_img(img_path)
                # cv2.imshow("test", img)
                # cv2.waitKey(0)

                pro_num = random.randint(1,3)
                pro_list = random_int_list(0, 5, pro_num)
                for k in range(len(pro_list)):
                    if pro_list[k] == 0:
                        img = processing.grey(img)
                    elif pro_list[k] == 1:
                        img = processing.pixel(img)
                    # elif pro_list[k] == 2:
                    #     img = processing.edgeDetection(img)
                    elif pro_list[k] == 2:
                        img = processing.expand(img)
                    elif pro_list[k] == 3:
                        img = processing.rotate(img)
                    elif pro_list[k] == 4:
                        img = processing.saltPepper(img)
                    elif pro_list[k] == 5:
                        img = processing.guass(img)

                out_file = out_path + challeng + '/' + image
                if not os.path.exists(out_path + challeng):
                    os.mkdir(out_path + challeng)
                cv2.imencode('.jpg', img)[1].tofile(out_file)
            except:
                out_file = out_path + challeng + '/' + image
                if not os.path.exists(out_path + challeng):
                    os.mkdir(out_path + challeng)
                    shutil.copyfile(img_path, out_path + challeng + '/' + image)
                    print(img_path)

def add_process_to_image():
    in_path = "D:/Lab_work_XCX/DATASET/VTT/csCAPTCHA/new_img/"
    out_path = "D:/Lab_work_XCX/DATASET/VTT/csCAPTCHA/new_img2/"
    imgs = os.listdir(in_path)
    num = 0
    for imgg in imgs:
        num += 1
        print(num)
        if num > 35000:
            images = in_path + imgg
            try:
                img = processing.read_img(images)
                # cv2.imshow("test", img)
                # cv2.waitKey(0)

                pro_num = random.randint(1,3)
                pro_list = random_int_list(0, 5, pro_num)
                for k in range(len(pro_list)):
                    if pro_list[k] == 0:
                        img = processing.grey(img)
                    elif pro_list[k] == 1:
                        img = processing.pixel(img)
                    # elif pro_list[k] == 2:
                    #     img = processing.edgeDetection(img)
                    elif pro_list[k] == 2:
                         img = processing.expand(img)
                    elif pro_list[k] == 3:
                        img = processing.rotate(img)
                    elif pro_list[k] == 4:
                        img = processing.saltPepper(img)
                    elif pro_list[k] == 5:
                        img = processing.guass(img)

                out_file = out_path + imgg
                cv2.imencode('.jpg', img)[1].tofile(out_file)
            except:
                out_file = out_path + imgg
                shutil.copyfile(images, out_file)
                print(images)

def add_process_to_classed_images():
    in_path = "D:/Lab_work_XCX/DATASET/VTT/cs/"
    out_path = "D:/Lab_work_XCX/A-VTT/experiment/imgProcess/afterpro_data/"

    files = os.listdir(in_path)
    cls_num = len(files)
    for i in range(cls_num):
        file = in_path + files[i]
        f = os.listdir(file)
        file_num = len(f)
        print(i)

        for j in range(file_num):
            img_path = file + '/' + f[j]
            try:
                img = processing.read_img(img_path)
                # cv2.imshow("test", img)
                # cv2.waitKey(0)

                pro_num = random.randint(2,4)
                pro_list = random_int_list(0, 5, pro_num)
                for k in range(len(pro_list)):
                    if pro_list[k] == 0:
                        img = processing.grey(img)
                    elif pro_list[k] == 1:
                        img = processing.pixel(img)
                    # elif pro_list[k] == 2:
                    #     img = processing.edgeDetection(img)
                    elif pro_list[k] == 2:
                        img = processing.expand(img)
                    elif pro_list[k] == 3:
                        img = processing.rotate(img)
                    elif pro_list[k] == 4:
                        img = processing.saltPepper(img)
                    elif pro_list[k] == 5:
                        img = processing.guass(img)

                out_file =  out_path + files[i] + '/' + f[j]
                if not os.path.exists(out_path + files[i]):
                    os.mkdir(out_path + files[i])
                cv2.imencode('.jpg', img)[1].tofile(out_file)
            except:
                shutil.copyfile(img_path, out_path + files[i] + '/' + f[j])
                print(img_path)

if __name__ == "__main__":
    challenge_path = ""
    out_path = ""
    add_process_to_challenge(challenge_path, out_path)