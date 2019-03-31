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
	# Prophet算法
	# x = [5, 10, 15, 20, 25] 	# SprayAndWait算法消息缓存大小
	# y = [10.7304, 7.0421, 6.2179, 5.9821, 5.8933] 	# SprayAndWait算法负载率
	x2 =  [2, 4, 6, 8, 10]  # Prophet算法消息缓存大小
	y2 = [60.8092, 70.0497, 67.7918, 61.5911, 56.6225]  # 消息负载率
	x3 =  [2, 4, 6, 8, 10]  # Propose算法消息缓存大小
	y3 = [5.7195, 2.8535, 2.2291, 1.9699, 1.8750]		# 消息负载率
	fig_size = (5,5)
	mpl.rcParams['figure.figsize'] = fig_size
	fig, ax = plt.subplots()
	xmajorLocator = MultipleLocator(5)  # 将y轴主刻度标签设置为100 * 2的倍数
	# plt.plot(x, y, '-ok', label='SprayAndWait', linewidth=2, color='#000000',
	#			markeredgewidth=1,  markersize=8)
	plt.plot(x2, y2, '-^k', label='Epidemic', linewidth=2, color='#0000FF',
			 markeredgewidth=1, markersize=8)
	plt.plot(x3, y3, '-sk', label='Prophet', linewidth=2, color='#FF0000',
			 markeredgewidth=1, markersize=8)
	plt.ticklabel_format(style='plain', axis='y', scilimits=(0, 0))
	plt.grid(False)
	plt.xlabel(u'消息缓存大小', fontsize=15)
	plt.ylabel(u'负载率', fontsize=15)
	plt.ylim(5, 90)
	plt.xlim(left=5, right=30)
	plt.legend(loc='upper right')
	plt.show()
	return

if __name__ == '__main__':
	main()
