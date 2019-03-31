#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Plot a figure from a batch of MessageStatsReports
'''
import matplotlib.pyplot as plt

import numpy as np

from matplotlib.ticker import MultipleLocator
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False


def main():
    # Step 1: Read files
    # Get filenames
    # Read files
    # SprayAndWait算法、Epidemic算法、Prophet算法
    # x = [200, 250, 300, 350, 400] 	# SprayAndWait算法消息生存周期
    # y = [11.0190, 10.8474, 10.7304, 10.5515, 10.5356] 	# SprayAndWait算法负载率
    # x2 = [200, 250, 300, 350, 400]  # Epidemic算法消息生存周期
    # y2 = [76.7360, 78.4278, 83.9539, 92.3652, 98.8486]
    # x3 = [200, 250, 300, 350, 400]  # Prophet算法消息生存周期
    # y3 = [56.3858, 62.3930, 64.5131, 74.1475, 79.3118]


    # fig_size = (5,5)
    # mpl.rcParams['figure.figsize'] = fig_size
    # fig, ax = plt.subplots()
    # xmajorLocator = MultipleLocator(5)  # 将y轴主刻度标签设置为100 * 2的倍数
    # plt.plot(x, y, '-ok', label='SprayAndWait', linewidth=2, color='#000000',
    #          markeredgewidth=1,  markersize=8)
    # plt.plot(x2, y2, '-^k', label='Epidemic', linewidth=2, color='#0000FF',
    #          markeredgewidth=1, markersize=8)
    # plt.plot(x3, y3, '-sk', label='Prophet', linewidth=2, color='#FF0000',
    #          markeredgewidth=1, markersize=8)
    plt.ticklabel_format(style='plain', axis='y', scilimits=(0, 0))
    plt.grid(False)
    plt.xlabel(u'消息生存周期', fontsize=15)
    plt.ylabel(u'负载率', fontsize=15)
    plt.ylim(5, 100)
    plt.xlim(left=180, right=420)
    plt.legend(loc='upper left')
    plt.show()
    return

if __name__ == '__main__':
	main()
