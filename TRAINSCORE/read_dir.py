"""
this py is functioned as the tool in order to draw out the pic_names in a samples file, into a dict type
and saved as a txt
which used for re extraction in trail.py

"""
import os
def draw_up():
    filetype = input("please input the type of samples \nfor example:'0' stands for the 'no-mask"
                     "and '1' stands for the 'mask' : ")
    filepath = "C:\\Users\\Breeze\\Desktop\\keras-yolo3-master\\TRAINSCORE\\"+filetype+"\\"
    newtxt = input("Please input the name of the new txt you want to create \nfor example:'demo%d.txt' : ")
    address = "C:\\Users\\Breeze\\Desktop\\keras-yolo3-master\\TRAINSCORE\\"+newtxt
    fw = open(address, 'w')
    print("-----------------------")
    print("File: {} .file is created".format(filetype))
    fw.truncate()
    num = 0
    for i,j,k in os.walk(filepath):
        for dire in k:
            fw.write(str(k)+'\n')
            break
    print("-----------------------")
    print("File: {} .txt is created".format(newtxt))
    fw.close()
    return filetype
# fw = open("C:\\Users\\Breeze\\Desktop\\keras-yolo3-master\\TRAINSCORE\\demo.txt", 'r')
# res=[]
# for line in fw.readlines():
#    print(line)
