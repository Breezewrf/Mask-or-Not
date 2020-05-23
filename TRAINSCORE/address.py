import os

filepath = "C:\\Users\\Breeze\\Desktop\\keras-yolo3-master\\VOCdevkit\\VOC2020\\ImageSets\\Main\\test.txt"

address = "C:\\Users\\Breeze\\Desktop\\darknet\\darknet-master\\build\darknet\\x64\\data\\test_voc.txt"
os.remove(address)
fr = open(filepath, 'r')
fw = open(address,'w')

adds=fr.readlines()

for add in adds:
    a=eval(add)
    t="C:\\Users\\Breeze\\Desktop\\keras-yolo3-master\\VOCdevkit\\VOC2020\\JPEGImages\\{}.jpg\n".format(a)
    fw.write(t)
fr.close()
fw.close()
