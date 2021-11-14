#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 19:32:19 2021

@author: mrk
"""

import matplotlib.pyplot as plt
import numpy as np

def plotting1():
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
    
    fig.tight_layout()
    fig.savefig("../plots/1.pdf")
    
def plotting2():
    data1 = np.genfromtxt('../data/2_1.txt')
    data2 = np.genfromtxt('../data/2_2.txt')
    data3 = np.genfromtxt('../data/2_3.txt')
    
    fig = plt.figure(figsize=(7,5))
    ax = fig.add_subplot(1,1,1)
    ax.errorbar(data1[:,0]*0.5, data1[:,1], xerr=0.25, yerr=0.005, c="tomato",
                lw=1, linestyle='dashed', marker='v', ecolor="tomato",
                label=r'$V_з = 40$ B')
    ax.errorbar(data2[:,0]*0.5, data2[:,1], xerr=0.25, yerr=0.005, c="teal",
                lw=1, linestyle='dashed', marker='p', ecolor="teal",
                label=r'$V_з = 45$ B')
    ax.errorbar(data3[:,0]*0.5, data3[:,1], xerr=0.25, yerr=0.005, c="sienna",
                lw=1, linestyle='dashed', marker='*', ecolor="sienna",
                label=r'$V_з = 50$ B')
    
    ax.set_ylim([-0.01,1.01])
    ax.set_xlim([19.5,31.5])
    ax.set_yticks(np.arange(0,11)/10)
    ax.set_xticks([20,21,22,23,24,25,26,27,28,29,30,31])
    # ax.grid()
    
    ax.set_ylabel("Анодный ток, мА")
    ax.set_xlabel("Ускоряющий потенциал, В")
    ax.legend()
    
    # linear regression
    cond = data1[:,0] * 0.5 > 25
    x1 = np.take(data1[:,0]*0.5, np.nonzero(cond))
    y1 = np.take(data1[:,1], np.nonzero(cond))
    
    cond = data2[:,0] * 0.5 > 25
    x2 = np.take(data2[:,0]*0.5, np.nonzero(cond))
    y2 = np.take(data2[:,1], np.nonzero(cond))
    
    cond = data3[:,0] * 0.5 > 25
    x3 = np.take(data3[:,0]*0.5, np.nonzero(cond))
    y3 = np.take(data3[:,1], np.nonzero(cond))
    
    x = np.append(x1, x2)
    x = np.append(x, x3)
    
    y = np.append(y1, y2)
    y = np.append(y, y3)
    
    p1 = np.poly1d(np.polyfit(x, y, 1))
    
    ax.plot(np.arange(24,32), p1(np.arange(24,32)), color='black',
            linestyle='-.')
    
    fig.tight_layout()
    fig.savefig("../plots/2.pdf")
    

if __name__ == "__main__":
    # plotting1()
    plotting2()
    