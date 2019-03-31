# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
# 功能：将txt文本中的 关键字 和 对应的值 取出，存成字典类型
import glob
import os
# path = './mydata/prophet'

def print_File(input_file):
    reader = open(input_file,'r')
    dic = {}
    line = reader.readline()    #  忽略第一行
    while True:
        line = reader.readline()
        if len(line) == 0:
            break
        # print(line)
        s = line.split(': ')
        dic[s[0]] = s[1].strip()
    print(dic['delivery_prob'])
    reader.close()

def main(path):
    cate = [path + '/' + x for x in os.listdir(path)]
    for idx, folder in enumerate(cate):
        for im in glob.glob(folder + '/*.txt'):
            print_File(im)

if __name__ == '__main__':
    main('./mydata/prophet')
