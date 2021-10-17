#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 19:12:23 2021

@author: mrkozelberg
"""

import matplotlib.pyplot as plt
from scipy.constants import c
import numpy as np

data = np.genfromtxt("../data/2.txt")

l = c / (data[:,1] * 10**(14)) 

fig = plt.figure(figsize = (9,6))
ax = fig.add_subplot(1,1,1)
ax.set_title("Ширина входной щели 0.37 мм, ширина выходной щели 0.03 мм")
ax.errorbar(data[:,1], data[:,2] - data[0,2], c = 'red')
# ax.errobar(data[:,1], data[:,2], yerr = data[0,2])
ax.set_ylabel("Фототок, деления")
ax.set_xlabel(r'Частота света, $10^{-14}$ Гц')
ax.grid()

fig.savefig('../plots/2.png', dpi = 300, bbox_inches = 'tight')