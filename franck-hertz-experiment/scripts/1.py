#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 19:32:19 2021

@author: mrk
"""

import matplotlib.pyplot as plt

import numpy as np

from scipy.constants import e

def plotting(data):
    fig = plt.figure(figsize=(7,5))
    ax = fig.add_subplot(111)
    ax.errorbar(data[:,0], data[:,1]*50, xerr=1/2, yerr=0.5/2, c="gray",
                lw=1, ecolor="red")
    ax.set_ylabel("Анодный ток, мА")
    ax.set_xlabel("Ускоряющее напряжение, В")
    # ax.set_title("Анодно-сеточная характеристика\nпри задерживающем напряжении 12.1 В")
    fig.tight_layout()
    fig.savefig("../plots/1.pdf")

if __name__ == "__main__":
    data = np.genfromtxt("../data/1.txt")
    plotting(data)
    # We could find first two local maxima on 24 and 48 V
    print('E_1 - E_0 = {:.3} эВ'.format(24*e))
    