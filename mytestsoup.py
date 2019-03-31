
#读取输入的词条，并输出百度百科里该词条的简介部分。

import re
import urllib.request
from bs4 import BeautifulSoup
import urllib.parse

# search_item为输入词条，进入while循环可一直搜索，当输入为'out'时退出。
search_item = input("Enter what you want(Enter 'out' to exit):")
while search_item != 'out':
    if search_item == 'out':
        exit(0)
    print("please wait...")
    try:
        url = 'https://baike.baidu.com/item/'+urllib.parse.quote(search_item)
        # 读取网页部分
        html = urllib.request.urlopen(url)      # 打开链接，读取网页
        content = html.read().decode('utf-8')   # 设置编码格式
        html.close()
        ####
        # 网页解析部分
        soup = BeautifulSoup(content, "lxml")  # 利用BeautifulSoup为网页解析
        # text为该词条的百度百科简介的网页形式，通过正则表达式将其中的文字提取出来
        text = soup.find('div', class_="lemma-summary").children    # 解析百度百科词条中简介部分
        ####
        print("search result:")
        # 文本处理部分
        for x in text:
            # 用python中的re模块检查一个特定的字符串是否匹配给定的正则表达式
            word = re.sub(re.compile(r"<(.+?)>"),'',str(x))
            words = re.sub(re.compile(r"\[(.+?)\]"),'',word)
            print(words,'\n')
        ######
    # 异常处理
    except AttributeError:
        # 如果百度百科里没有该词条，输出失败信息，并提示测试这将词条具体化些再输入
        print("Failed!Please enter more in details!")
    search_item = input("Enter what you want(Enter 'out' to exit):")
