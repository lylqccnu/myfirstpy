# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import glob
import os
path = './mydata/prophet'

def read_File(path):
    cate = [path + '/' + x for x in os.listdir(path)]
    for idx, folder in enumerate(cate):
        for im in glob.glob(folder + '/*.txt'):
            f1 = open(im, 'r')
            for eachLine in f1:
                print(eachLine)
            f1.close()
read_File(path)