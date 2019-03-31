#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
allFileNum = 0
def printPath(level, path):
    global allFileNum
    '''
    打印一个目录下的所有文件夹和文件
    '''
    # 所有文件夹，第一个字段是次目录的级别
    dirList = []
    # 所有文件
    fileList = []
    # 返回一个列表，其中包含在目录条目的名称
    files = os.listdir(path)
    # 先添加目录级别
    dirList.append(str(level))
    for f in files:
        if(os.path.isdir(path + '/' + f)):
            if(f[0] == '.'):
                pass
            else:
                dirList.append(f)
        if(os.path.isfile(path + '/' + f)):
            fileList.append(f)
    i_dl = 0
    for dl in dirList:
        if(i_dl == 0):
            i_dl = i_dl + 1
        else:
            print('-' * (int(dirList[0])), dl)
            printPath((int(dirList[0]) + 1), path + '/' + dl)
    for fl in fileList:
        print('-' *  (int(dirList[0])), fl)
        # print(fl)
        allFileNum = allFileNum + 1
if __name__ == '__main__':
    printPath(1, './mydata/prophet')
    print ('总文件数 = ', allFileNum)
