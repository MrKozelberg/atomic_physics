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
    
    p = np.poly1d(np.polyfit(data[:,0], data[:,1], 13))
    x = data[:,0]
    y = p(x)
    
    
    fig = plt.figure(figsize=(9,6))
    ax = fig.add_subplot(111)
    ax.errorbar(data[:,0], data[:,1], xerr=0.75, yerr=0.5, linestyle=' ',
                lw=1, ecolor="black")
    ax.plot(x, y, color='black', linestyle='-', label='Аппроксимация полиномом 13 степени')
    
    ax.set_ylabel("Анодный ток, мА")
    ax.set_xlabel("Ускоряющий потенциал, В")
    
    ax.set_xlim([-1,56])
    ax.set_ylim(-1,70)
    # ax.set_xticks([0,10,20,30,40,50])
    # ax.set_xticklabels([0,10,20,30,40,50])
    
    ax.axvline(x=20.5, linewidth=1, color='black', linestyle='--', label=r'$\varphi_1$')
    ax.axvline(x=43.125, linewidth=1, color='black', linestyle='-.', label=r'$\varphi_2$')
    
    ax.legend()
    ax.grid()
    
    fig.tight_layout()
    fig.savefig("../plots/1.pdf")
    
    print(r'$\varphi_1 = {:}\pm{:.2}$'.format(20.50,np.sqrt(np.std([20,20.5,21])**2 + 0.75**2)))
    print(r'$\varphi_2 = {:}\pm{:.2}$'.format(43.13,np.sqrt(np.std([42,43,43.5,44])**2 + 0.75**2)))
    
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
    
    min_i = 27
    
    # linear regression
    cond = data1[:,0] * 0.5 > min_i
    x1 = np.take(data1[:,0]*0.5, np.nonzero(cond))
    y1 = np.take(data1[:,1], np.nonzero(cond))
    
    cond = data2[:,0] * 0.5 > min_i
    x2 = np.take(data2[:,0]*0.5, np.nonzero(cond))
    y2 = np.take(data2[:,1], np.nonzero(cond))
    
    cond = data3[:,0] * 0.5 > min_i
    x3 = np.take(data3[:,0]*0.5, np.nonzero(cond))
    y3 = np.take(data3[:,1], np.nonzero(cond))
    
    x = np.append(x1, x2)
    x = np.append(x, x3)
    
    y = np.append(y1, y2)
    y = np.append(y, y3)
    
    print('{:.2f}'.format(np.std(y)))
    
    p1 = np.poly1d(np.polyfit(x, y, 1))
    
    ax.plot(np.linspace(20,31,2), p1(np.linspace(20,31,2)), color='black',
            linestyle='-.')
    
    max_i = 24
    
    # linear regression
    cond = data1[:,0] * 0.5 < max_i
    x1 = np.take(data1[:,0]*0.5, np.nonzero(cond))
    y1 = np.take(data1[:,1], np.nonzero(cond))
    
    cond = data2[:,0] * 0.5 < max_i
    x2 = np.take(data2[:,0]*0.5, np.nonzero(cond))
    y2 = np.take(data2[:,1], np.nonzero(cond))
    
    cond = data3[:,0] * 0.5 < max_i
    x3 = np.take(data3[:,0]*0.5, np.nonzero(cond))
    y3 = np.take(data3[:,1], np.nonzero(cond))
    
    x = np.append(x1, x2)
    x = np.append(x, x3)
    
    y = np.append(y1, y2)
    y = np.append(y, y3)
    
    print('{:.2f}'.format(np.std(y)))
    
    p1 = np.poly1d(np.polyfit(x, y, 1))
    
    ax.plot(np.linspace(16,35,2), p1(np.linspace(16,35,2)), color='black',
            linestyle='--')
    
    fig.tight_layout()
    fig.savefig("../plots/2.pdf")
    

if __name__ == "__main__":
    plotting1()
    # plotting2()
    