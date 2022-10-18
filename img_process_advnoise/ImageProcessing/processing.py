import os
import random
import shutil
import cv2
import numpy as np

# 1. Graying
def grey(img):
    if len(img.shape) == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img
    return gray

# # 2. Image binary
# def binary(img):
#     gary = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     ret , bin = cv2.threshold(gary,130,255,cv2.THRESH_BINARY)
#     return bin

# 3. Motion blur
def motionBlur(img, degree=5, angle=30):
    image = img.copy()
    # The higher the degree, the higher the blur
    M = cv2.getRotationMatrix2D((degree / 2, degree / 2), angle, 1)
    motion_blur_kernel = np.diag(np.ones(degree))
    motion_blur_kernel = cv2.warpAffine(motion_blur_kernel, M, (degree, degree))

    motion_blur_kernel = motion_blur_kernel / degree
    blurred = cv2.filter2D(image, -1, motion_blur_kernel)
    # convert to uint8
    cv2.normalize(blurred, blurred, 0, 255, cv2.NORM_MINMAX)
    blurred = np.array(blurred, dtype=np.uint8)
    return blurred

# 4. Fuzzy clustering Method
def meanBlur(img):
    dst = cv2.blur(img,(3,3))
    return dst

# 5.Pixelation
def pixel(img):
    le = 2
    if len(img.shape) == 3:
        height, width, deep = img.shape
        for m in range(height - le):
            for n in range(width - le):
                if m % le == 0 and n % le == 0:
                    for i in range(le):
                        for j in range(le):
                            b, g, r = img[m, n]
                            img[m + i, n + j] = (b, g, r)
    return img

# 6.Edge detection
def edgeDetection(img):
    canny = cv2.Canny(img, 138, 200)
    return canny

# # 7. Emboss
# def relief(img, file_path):
#     ret , bin = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
#     return bin

# 8. Erosion
def erosion(img):
    conv_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 4))
    img_erod = cv2.erode(img, conv_kernel)
    return img_erod

# 9. Dilate
def expand(img):
    conv_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 4))
    img_dilate= cv2.dilate(img, conv_kernel)
    return img_dilate

# 10. Rotation
def rotate(img):
    transpose = cv2.transpose(img)
    return transpose

# 11. Image fusion
def fusion(img1, img2):
    H, W, C = img1.shape
    img2 = cv2.resize(img2, (W, H))
    a = 0.85
    out = img1 * a + img2 * (1 - a)
    out = out.astype(np.uint8)
    return out

# 12. Impulse noise
def saltPepper(img):
    if len(img.shape) == 3:
        percentage = 0.005
        num = int(percentage * img.shape[0] * img.shape[1])
        random.randint(0, img.shape[0])
        img2 = img.copy()
        for i in range(num):
            X = random.randint(0, img2.shape[0] - 1)
            Y = random.randint(0, img2.shape[1] - 1)
            if random.randint(0, 1) == 0:
                img2[X, Y] = (255, 255, 255)
            else:
                img2[X, Y] = (0, 0, 0)
    else:
        img2 = img
    return img2

# 13. Gaussian noise
def guass(img):
    mean = 0
    var = 0.003
    img = np.array(img / 255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, img.shape)
    out_img = img + noise
    if out_img.min() < 0:
        low_clip = -1
    else:
        low_clip = 0
    out_img = np.clip(out_img, low_clip, 1.0)
    out_img = np.uint8(out_img * 255)
    return out_img

# Read the Chinese name image
def read_img(img_path):
    cv_img = cv2.imdecode(np.fromfile(img_path,dtype=np.uint8),-1)
    return cv_img

# path_file = "D:/Lab_work_XCX/DATASET/VTT/csCAPTCHA/2.0/test/Challenge0/"
# files = os.listdir(path_file)
# i = 0
# for i in range(0, len(files)):
#         file1 = path_file + files[i]
#         img1 = read_img(file1)
#         print(str(i) + "：" + str(file1))
#         # read img2
#         # x = random.randint(0, len(files)-1)
#         # file2 = path_file + files[x]
#         # img2 = read_img(file2)
#
#         # img_test = "D:/Lab_work_XCX/A-VTT/experiment/imgProcess/data/test/t.png"
#         # img_t = cv2.imread(img_test)
#         # print(img_t)
#         # cv2.imshow('img', img_t)
#         # cv2.waitKey(0)
#
#         # out = grey(img1)
#         # out = motionBlur(img1)
#         # out = meanBlur(img1)
#         out = pixel(img1)
#         # out = edgeDetection(img1)
#         # out = erosion(img1)
#         # out = expand(img1)
#         # out = rotate(img1)
#         # out = fusion(img1, img2)
#         # out = saltPepper(img1)
#         # out = guass(img1)
#         out_path = "D:/Lab_work_XCX/DATASET/VTT/csCAPTCHA/2.0/image2/" + files[i]
#         cv2.imencode('.jpg', out)[1].tofile(out_path)
#         cv2.imwrite(out_path , out)