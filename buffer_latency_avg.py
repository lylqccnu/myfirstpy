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
	x = [5, 10, 15, 20, 25] 	# SprayAndWait算法消息缓存大小
	y = [2997, 4082, 4672, 4925, 5048] 	# SprayAndWait算法平均时延
	x2 = [5, 10, 15, 20, 25]  # Epidemic算法消息缓存大小
	y2 = [4703, 5372, 5983, 6540, 7032]	 # Epidemic算法算法平均时延
	x3 = [5, 10, 15, 20, 25]  # Prophet算法消息缓存大小
	y3 = [4753, 5100, 5492, 6044, 6224]  # Prophet算法平均时延
	fig_size = (5,5)
	mpl.rcParams['figure.figsize'] = fig_size
	fig, ax = plt.subplots()
	xmajorLocator = MultipleLocator(5)  # 将y轴主刻度标签设置为100 * 2的倍数
	plt.plot(x, y, '-ok', label='SprayAndWait', linewidth=2, color='#000000',
				markeredgewidth=1,  markersize=8)
	plt.plot(x2, y2, '-^k', label='Epidemic', linewidth=2, color='#0000FF',
			 markeredgewidth=1, markersize=8)
	plt.plot(x3, y3, '-sk', label='Prophet', linewidth=2, color='#FF0000',
			 markeredgewidth=1, markersize=8)
	plt.ticklabel_format(style='plain', axis='y', scilimits=(0, 0))
	plt.grid(False)
	plt.xlabel(u'消息缓存大小', fontsize=15)
	plt.ylabel(u'平均时延', fontsize=15)
	plt.ylim(2000, 8000)
	plt.xlim(left=0, right=30)
	plt.legend(loc='upper left')
	plt.show()
	return

if __name__ == '__main__':
	main()
