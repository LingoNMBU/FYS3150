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

#1. Importing data

x10 = pd.read_csv(r'Prob7_x10')
u10 = pd.read_csv(r'Prob7_u10')
v10 = pd.read_csv(r'Prob7_v_gen10')
t10 = pd.read_csv(r'Prob7_time10')

x102 = pd.read_csv(r'Prob7_x100')
u102 = pd.read_csv(r'Prob7_u100')
v102 = pd.read_csv(r'Prob7_v_gen100')
t102 = pd.read_csv(r'Prob7_time100')

x103 = pd.read_csv(r'Prob7_x1000')
u103 = pd.read_csv(r'Prob7_u1000')
v103 = pd.read_csv(r'Prob7_v_gen1000')
t103 = pd.read_csv(r'Prob7_time1000')

x104 = pd.read_csv(r'Prob7_x10000')
u104 = pd.read_csv(r'Prob7_u10000')
v104 = pd.read_csv(r'Prob7_v_gen10000')
t104 = pd.read_csv(r'Prob7_time10000')

x105 = pd.read_csv(r'Prob7_x100000')
u105 = pd.read_csv(r'Prob7_u100000')
v105 = pd.read_csv(r'Prob7_v_gen100000')
t105 = pd.read_csv(r'Prob7_time100000')

x106 = pd.read_csv(r'Prob7_x1000000')
u106 = pd.read_csv(r'Prob7_u1000000')
v106 = pd.read_csv(r'Prob7_v_gen1000000')
t106 = pd.read_csv(r'Prob7_time1000000')

x107 = pd.read_csv(r'Prob7_x10000000')
u107 = pd.read_csv(r'Prob7_u10000000')
v107 = pd.read_csv(r'Prob7_v_gen10000000')
t107 = pd.read_csv(r'Prob7_time10000000')

npoints = [10, 10e2, 10e3, 10e4, 10e5]
x_values = [x10, x102, x103, x104, x105]
u_values = [u10, u102, u103, u104, u105]
v_values = [v10, v102, v103, v104, v105]

# Plotting solutions
f1, ax1 = plt.subplots(figsize=(12, 8))
ax1.set_ylim(0, 0.7)
for i in range(len(u_values)):
    ax1.plot(x_values[i].values, u_values[i].values, label=f'exact solution {int(npoints[i])} points')
    ax1.plot(x_values[i].values, v_values[i].values, label=f'algorithm solution {int(npoints[i])} points', linestyle='dashed')
ax1.set_title('Exact vs. algorithm')
ax1.legend()
plt.xlabel('x-value')
plt.ylabel('u-value')
plt.savefig('solution_plots.pdf')
plt.show()


def log_error(u, v):
    """
    Calculate logarithmic error
    :param u: exact solution
    :param v: model solution
    :return:
    """
    errors = np.zeros(len(u))
    k = 0
    for i, j in zip(u, v):
        if i - j == 0:
            errors[k] = 0
            k += 1
        else:
            errors[k] = np.log(abs(i - j))[:]
            k += 1
    return errors


def rel_error(u, v):
    """
    Calculates relative error
    :param u: exact value
    :param v: model value
    :return:
    """
    errors = np.zeros(len(u))
    k = 0
    for i, j in zip(u, v):
        if i - j == 0:
            errors[k] = 0
            k += 1
        else:
            relres = (i - j) / i
            errors[k] = np.log(abs((relres)))[:]
            k += 1
    return errors

# error calc points
npoints2 = [10, 10e2, 10e3, 10e4, 10e5, 10e6]
x_values2 = [x10, x102, x103, x104, x105, x106]
u_values2 = [u10, u102, u103, u104, u105, u106]
v_values2 = [v10, v102, v103, v104, v105, v106]

# max error points
# npoints2 = [10, 10e2, 10e3, 10e4, 10e5, 10e6, 10e7]
# x_values2 = [x10, x102, x103, x104, x105, x106, x107]
# u_values2 = [u10, u102, u103, u104, u105, u106, u107]
# v_values2 = [v10, v102, v103, v104, v105, v106, v107]

# npoints2 = [10, 10e2, 10e3]
# x_values2 = [x10, x102, x103]
# u_values2 = [u10, u102, u103]
# v_values2 = [v10, v102, v103]

# plotting log error
f2, ax2 = plt.subplots(figsize=(12, 8))
for i in range(len(u_values2)):
    ax2.plot(x_values2[i].values[0:-1], log_error(u_values2[i].values[0:-1], v_values2[i].values[0:-1]),
              label=f'{int(npoints2[i])} points', linestyle='dashed')
ax2.set_title('Logarithmic errors')
ax2.legend()
plt.xlabel('x-value')
plt.ylabel('log(Error)')
plt.savefig('log_errors.pdf')
plt.show()

# plotting relative error and calculating max relative error
max_relative_errors = {}
f3, ax3 = plt.subplots(figsize=(12, 8))
for i in range(len(u_values2)):
    rel_error_i = rel_error(u_values2[i].values[0:-1], v_values2[i].values[0:-1])
    ax3.plot(x_values2[i].values[0:-1], rel_error_i,
             label=f'{int(npoints2[i])} points', linestyle='dashed')

    max_relative_errors[f'{npoints2[i]}points'] = np.max(rel_error_i)
ax3.set_title('Relative errors')
ax3.legend()
plt.xlabel('x-value')
plt.ylabel('log(Error)')
plt.savefig('rel_errors.pdf')
plt.show()

# saving max error file
max_rel_err_df = pd.DataFrame(max_relative_errors, index=['max_errors'])
max_rel_err_df.to_csv('max_rel_err.txt', sep='\t')
