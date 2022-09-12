# !python
# -*- coding: utf-8 -*

__author__ = 'Erling Ween Eriksen'
__email__ = 'erlinge@nmbu.no'

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pyarma as arma
import sys
import os

working_dir = os.getcwd()

fvals10 = pd.read_csv(r'C:\Users\erlin\Desktop\Studie\2021\VÅR\FYS3150\Prob7_f_values_10steps')
fvals10_alg_df = pd.read_csv(r'C:\Users\erlin\Desktop\Studie\2021\VÅR\FYS3150'
                             r'\Prob7_function_values_10steps')

fvals100 = pd.read_csv(r'C:\Users\erlin\Desktop\Studie\2021\VÅR\FYS3150\Prob7_f_values_100steps')
fvals100_alg_df = pd.read_csv(r'C:\Users\erlin\Desktop\Studie\2021\VÅR\FYS3150'
                              r'\Prob7_function_values_100steps')

fvals1000 = pd.read_csv(r'C:\Users\erlin\Desktop\Studie\2021\VÅR\FYS3150\Prob7_f_values_1000steps')
fvals1000_alg_df = pd.read_csv(r'C:\Users\erlin\Desktop\Studie\2021\VÅR\FYS3150'
                               r'\Prob7_function_values_1000steps')

fvals100000 = pd.read_csv(r'C:\Users\erlin\Desktop\Studie\2021\VÅR\FYS3150'
                          r'\Prob7_f_values_100000steps')
fvals100000_alg_df = pd.read_csv(r'C:\Users\erlin\Desktop\Studie\2021\VÅR\FYS3150'
                                 r'\Prob7_function_values_100000steps')
xvals100000 = fvals100000.iloc[0:99999]
xvals1000 = fvals1000.iloc[0:999]
xvals100 = fvals100.iloc[0:99]
xvals10 = fvals10.iloc[0:9]

fvals100000 = fvals100000.iloc[100000:]
fvals100000_alg = fvals100000_alg_df.iloc[100000:]

fvals1000 = fvals1000.iloc[1000:]
fvals1000_alg = fvals1000_alg_df.iloc[1000:]

fvals100 = fvals100.iloc[100:]
fvals100_alg = fvals100_alg_df.iloc[100:]

fvals10 = fvals10.iloc[10:]
fvals10_alg = fvals10_alg_df.iloc[10:]

f10, ax10 = plt.subplots(figsize=(12, 8))
ax10.plot(xvals10, fvals10, label='exact solution')
ax10.plot(xvals10, fvals10_alg, label='algorithm solution', linestyle='dashed')
ax10.set_ylim(0, 0.7)
ax10.set_title('1000 points')
ax10.legend()
plt.xlabel('x-value')
plt.ylabel('u-value')
plt.show()

f100, ax100 = plt.subplots(figsize=(12, 8))
ax100.plot(xvals100, fvals100, label='exact solution')
ax100.plot(xvals100, fvals100_alg, label='algorithm solution', linestyle='dashed')
ax100.set_ylim(0, 0.7)
ax100.set_title('1000 points')
ax100.legend()
plt.xlabel('x-value')
plt.ylabel('u-value')
plt.show()

f1000, ax1000 = plt.subplots(figsize=(12, 8))
ax1000.plot(xvals1000, fvals1000, label='exact solution')
ax1000.plot(xvals1000, fvals1000_alg, label='algorithm solution', linestyle='dashed')
ax1000.set_ylim(0, 0.7)
ax1000.set_title('1000 points')
ax1000.legend()
plt.xlabel('x-value')
plt.ylabel('u-value')
plt.show()

f1000000, ax100000 = plt.subplots(figsize=(12, 8))
ax100000.plot(xvals100000, fvals100000, label='exact solution')
ax100000.plot(xvals100000, fvals100000_alg, label='algorithm solution', linestyle='dashed')
ax100000.set_ylim(0, 0.7)
ax100000.set_title('1000 points')
ax100000.legend()
plt.xlabel('x-value')
plt.ylabel('u-value')
plt.show()
