#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 19:32:19 2021

@author: mrk
"""

import matplotlib.pyplot as plt
import numpy as np

def plotting():
    data = np.genfromtxt("../data/1.txt")
    fig = plt.figure(figsize=(7,5))
    ax = fig.add_subplot(111)
    ax.errorbar(data[:,0], data[:,1]*50, xerr=0.5, yerr=0.25, c="gray",
                lw=1, ecolor="red")
    ax.set_ylabel("Анодный ток, мА")
    ax.set_xlabel("Ускоряющий потенциал, В")
    ax.set_xlim([10,62])
    ax.set_ylim(2,20)
    ax.set_xticks([12,20,24,30,40,48,50,60])
    ax.set_xticklabels(['12','20',r'$\varphi_1$','30','40',r'$\varphi_2$','50','60'])
    ax.vlines(24, 2, 0.37*50, linestyle=':', color='black')
    ax.vlines(48, 2, 0.38*50, linestyle=':', color='black')
    # ax.set_title("Анодно-сеточная характеристика\nпри задерживающем напряжении 12.1 В")
    fig.tight_layout()
    fig.savefig("../plots/1.pdf")

if __name__ == "__main__":
    plotting()
    