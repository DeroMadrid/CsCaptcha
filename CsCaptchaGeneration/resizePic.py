'''
descrption: 对所有图片提前resize
date: 2018/12/26
'''
from __future__ import division
from PIL import Image
import os
import time

def resizePic(savepath):
    picnum = 0
    for file in os.listdir(savepath):
        bgimg = Image.new('RGB', (150, 150), 'white')
        try:
            img = Image.open(savepath + file, 'r')
            if (img.width > img.height):
                randWidth = 150
                img2 = img.resize((randWidth, int(img.height / (img.width / (randWidth * 1.0)))), Image.ANTIALIAS)
            else:
                randHeight = 150
                img2 = img.resize((int(img.width / (img.height / (randHeight * 1.0))), randHeight), Image.ANTIALIAS)
            bgimg.paste(img2, (int((bgimg.width - img2.width) / 2), int((bgimg.height - img2.height) / 2)))
            bgimg.save(savepath + file, quality=95)
        except:
            continue
        print('resize')
        picnum+=1
    return picnum

if __name__ == '__main__':
    savepath = './allimage/appliance/'
    filelist = []
    for file in os.listdir(savepath):
        filelist.append(file)
    print(str(filelist))
    i = 0
    while(i < len(filelist)):
        resizePic(savepath+filelist[i] + '/')
        print(filelist[i])
        i+=1
