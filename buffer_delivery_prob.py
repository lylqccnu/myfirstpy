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
	# Propose算法、Prophet算法
	x2 = [2, 4, 6, 8, 10]  # Prophet算法消息缓存大小
	y2 = [0.1791, 0.2338, 0.2659, 0.3076, 0.3459]	 # 消息投递率
	x3 = [2, 4, 6, 8, 10]  # Propose算法消息缓存大小
	y3 = [0.1681,0.3452, 0.4416, 0.4997, 0.5249]	 # 消息投递率
	fig_size = (5,5)
	mpl.rcParams['figure.figsize'] = fig_size
	fig, ax = plt.subplots()
	# xmajorLocator = MultipleLocator(5)  # 将y轴主刻度标签设置为100 * 2的倍数
	# plt.plot(x, y, '-ok', label='SprayAndWait', linewidth=2, color='#000000',
	# 			markeredgewidth=1,  markersize=8)
	plt.plot(x2, y2, '-^k', label='Prophet', linewidth=2, color='#0000FF',
			 markeredgewidth=1, markersize=8)
	plt.plot(x3, y3, '-sk', label='Propose', linewidth=2, color='#FF0000',
			 markeredgewidth=1, markersize=8)
	# x2 = [5, 15, 25, 30]  # STProphet算法消息缓存大小
	# y2 = [0.3172, 0.5140, 0.6179, 0.6535]
	# x3 = [5, 15, 25, 30] # Prophet算法消息缓存大小
	# y3 = [0.2509, 0.4060, 0.5031, 0.5236]
	# plt.plot(x2, y2, '-o', label='STProphet', linewidth=2, color='#0000FF',
	# 		 markeredgewidth=1, markersize=8)
	# plt.plot(x3, y3, '-sk', label='Prophet', linewidth=2, color='#FF0000',
	# 		 markeredgewidth=1, markersize=8)
	plt.ticklabel_format(style='plain', axis='y', scilimits=(0, 0))
	plt.grid(False)
	plt.xlabel(u'消息缓存大小', fontsize=15)
	plt.ylabel(u'投递率', fontsize=15)
	plt.ylim(0.2, 0.6)
	plt.xlim(left=2, right=12)
	plt.legend(loc='upper left')
	plt.show()
	return

if __name__ == '__main__':
	main()
