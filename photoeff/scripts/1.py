#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 14:54:16 2021

@author: mrkozelberg
"""

import matplotlib.pyplot as plt
import numpy as np

# 1500, 2000, 2500 grad => 4.61e-7, 5.12e-7, 5.94e-7 m
wl = [4.61e-7, 5.12e-7, 5.94e-7]

fig = plt.figure(figsize = (12,4))

ax1 = fig.add_subplot(1,3,1)
data1 = np.genfromtxt("../data/1_1500.txt")
ax1.set_title("Длина волны {} м,\n ширина выходной щели {} мм".format(wl[0], 0.175))
ax1.set_ylabel("Фототок насыщения, деления")
ax1.set_xlabel("Ширина входной щели, мм")
ax1.scatter(data1[:,0], data1[:,1], c='red')

a,b = np.polyfit(data1[:,0], data1[:,1],1)
x = np.linspace(0.1,1,10)
r = np.corrcoef(data1[:,0], data1[:,1])[0,1]
ax1.plot(x, a*x + b, label = "a = {:.2f},\nb = {:.2f},\nr = {:.2f}".format(a, b, r))

ax1.grid()
ax1.legend()

ax2 = fig.add_subplot(1,3,2)
data2 = np.genfromtxt("../data/1_2000.txt")
ax2.set_title("Длина волны {} м,\n ширина выходной щели {} мм".format(wl[1], 0.075))
ax2.set_xlabel("Ширина входной щели, мм")
ax2.scatter(data2[:,0], data2[:,1], c='red')

a,b = np.polyfit(data2[:,0], data2[:,1],1)
x = np.linspace(0.1,1,10)
r = np.corrcoef(data2[:,0], data2[:,1])[0,1]
ax2.plot(x, a*x + b, label = "a = {:.2f},\nb = {:.2f},\nr = {:.2f}".format(a, b, r))

ax2.grid()
ax2.legend()

ax3 = fig.add_subplot(1,3,3)
data3 = np.genfromtxt("../data/1_2500.txt")
ax3.set_title("Длина волны {} м,\n ширина выходной щели {} мм".format(wl[2], 0.037))
ax3.set_xlabel("Ширина входной щели, мм")
ax3.scatter(data3[:,0], data3[:,1], c='red')

a,b = np.polyfit(data3[:,0], data3[:,1],1)
x = np.linspace(0.1,1,10)
r = np.corrcoef(data3[:,0], data3[:,1])[0,1]
ax3.plot(x, a*x + b, label = "a = {:.2f},\nb = {:.2f},\nr = {:.2f}".format(a, b, r))

ax3.grid()
ax3.legend()

fig.savefig('../plots/1.png', dpi = 300, bbox_inches = 'tight')