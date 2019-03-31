# -*- coding: utf-8 -*-
import sys
import re
import urllib.request
from bs4 import BeautifulSoup
import urllib.parse
from PyQt5.QtWidgets import (QPushButton, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication)


class Example(QWidget):
    def __init__(self):  # 初始化
        super().__init__()
        self.initUI()

    def introduction(self, citiao):  # 词条的百度百科简介部分函數https://baike.baidu.com/item/
        url = 'https://baike.baidu.com/item/' + urllib.parse.quote(citiao)
        # 读取网页
        # urllib的request模块可以非常方便地抓取URL内容，
        # 也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：
        html = urllib.request.urlopen(url)
        content = html.read().decode('utf-8')
        html.close()
        # 解析网页
        soup = BeautifulSoup(content, "lxml")
        text = soup.find('div', class_="lemma-summary").children  # 简介部分
        intro_text = ''
        # 利用正则表达式进行文本处理
        for x in text:
            word = re.sub(re.compile(r"<(.+?)>"), '', str(x))
            words = re.sub(re.compile(r"\[(.+?)\]"), '', word)
            intro_text += words

        return intro_text  # 返回文本(str格式)

    def intro_final(self, citiao):  # 异常处理函數
        try:
            return self.introduction(citiao)
        except AttributeError:
            return "请再输入详细点，亲~~"

    def initUI(self):
        # GUI布局及控件放置
        search_label = QLabel("请输入搜索词条：")
        search_item = QLineEdit()
        btn1 = QPushButton("开始搜索", self)
        btn2 = QPushButton("清空", self)
        search_result = QTextEdit()
        grid = QGridLayout()
        grid.setSpacing(5)
        grid.addWidget(search_label, 1, 0)
        grid.addWidget(search_item, 2, 0)
        grid.addWidget(btn1, 3, 0)
        grid.addWidget(btn2, 3, 1)
        grid.addWidget(search_result, 4, 0, 5, 0)
        self.setLayout(grid)

        # 设置按钮事件
        def searching():
            search_result.setText(self.intro_final(search_item.text()))
        # 搜索
        btn1.clicked.connect(searching)

        def clear():
            search_result.setText("")
            search_item.setText("")
        #清空
        btn2.clicked.connect(clear)

        # 設置窗口
        self.setGeometry(400, 150, 600, 500)
        self.setWindowTitle("百度百科搜索")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
