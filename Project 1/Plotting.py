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

npoints = [10, 10e2, 10e3, 10e4, 10e5, 10e6, 10e7]
x_values = [x10, x102, x103, x104, x105, x106, x107]
u_values = [u10, u102, u103, u104, u105, u106, u107]
v_values = [v10, v102, v103, v104, v105, v106, v107]


# f10, ax10 = plt.subplots(figsize=(12, 8))
# ax10.set_ylim(0, 0.7)
# for i in range(len(u_values)):
#
#    ax10.plot(x_values[i].values, u_values[i].values, label=f'exact solution {int(npoints[i])} points')
#    ax10.plot(x_values[i].values, v_values[i].values, label=f'algorithm solution {int(npoints[i])} points', linestyle='dashed')
#
# ax10.set_title('Exact vs. algorithm')
# ax10.legend()
# plt.xlabel('x-value')
# plt.ylabel('u-value')
# plt.show()


def log_error(u, v):
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


npoints2 = [10, 10e2, 10e3, 10e4, 10e5, 10e6]
x_values2 = [x10, x102, x103, x104, x105, x106]
u_values2 = [u10, u102, u103, u104, u105, u106]
v_values2 = [v10, v102, v103, v104, v105, v106]

#npoints2 = [10, 10e2, 10e3]
#x_values2 = [x10, x102, x103]
#u_values2 = [u10, u102, u103]
#v_values2 = [v10, v102, v103]


f2, ax2 = plt.subplots(figsize=(12, 8))
for i in range(len(u_values2)):
    ax2.plot(x_values2[i].values[0:-1], log_error(u_values2[i].values[0:-1], v_values2[i].values[0:-1]),
              label=f'{int(npoints[i])} points', linestyle='dashed')


f3, ax3 = plt.subplots(figsize=(12, 8))
for i in range(len(u_values2)):
    ax3.plot(x_values2[i].values[0:-1], rel_error(u_values2[i].values[0:-1], v_values2[i].values[0:-1]),
              label=f'{int(npoints[i])} points', linestyle='dashed')

ax3.set_title('Relative errors')
ax3.legend()
plt.xlabel('x-value')
plt.ylabel('log(Error)')
plt.show()

logerrors10 = log_error(fvals10, fvals10_alg)
logerrors100 = log_error(fvals100, fvals100_alg)
logerrors1000 = log_error(fvals1000, fvals1000_alg)
logerrors100000 = log_error(fvals100000, fvals100000_alg)

relerrors10 = rel_error(fvals10, fvals10_alg)
relerrors100 = rel_error(fvals100, fvals100_alg)
relerrors1000 = rel_error(fvals1000, fvals1000_alg)
relerrors100000 = rel_error(fvals100000, fvals100000_alg)

f210, ax10 = plt.subplots(figsize=(12, 8))
ax10.plot(xvals10, logerrors10, label='logarithmic error')
ax10.plot(xvals10, relerrors10, label='logarithmic relative error', linestyle='dashed')
ax10.set_title('10 points')
ax10.legend()
plt.xlabel('x-value')
plt.ylabel('Error')
plt.show()

f2100, ax2100 = plt.subplots(figsize=(12, 8))
ax2100.plot(xvals100, logerrors100, label='logarithmic error')
ax2100.plot(xvals100, relerrors100, label='logarithmic relative error', linestyle='dashed')
ax2100.set_title('100 points')
ax2100.legend()
plt.xlabel('x-value')
plt.ylabel('Error')
plt.show()

f21000, ax21000 = plt.subplots(figsize=(12, 8))
ax21000.plot(xvals1000, logerrors1000, label='logarithmic error')
ax21000.plot(xvals1000, relerrors1000, label='logarithmic relative error', linestyle='dashed')
ax21000.set_title('1000 points')
ax21000.legend()
plt.xlabel('x-value')
plt.ylabel('Error')
plt.show()

f21000000, ax2100000 = plt.subplots(figsize=(12, 8))
ax2100000.plot(xvals100000, logerrors100000, label='logarithmic error')
ax2100000.plot(xvals100000, relerrors100000, label='logarithmic relative error', linestyle='dashed')
ax2100000.set_title('100000 points')
ax2100000.legend()
plt.xlabel('x-value')
plt.ylabel('Error')
plt.show()
