# !python
# -*- coding: utf-8 -*

__author__ = 'Erling Ween Eriksen'
__email__ = 'erlinge@nmbu.no'

import matplotlib.pyplot as plt
import pandas as pd

xu = pd.read_csv('x_u_exact', delim_whitespace=True)
x = xu.iloc[:,0]
u = xu.iloc[:,1]

f, ax = plt.subplots(figsize=(12, 8), label= 'u(x)')
ax.plot(x,u)
ax.set_title('Analytic Solution of the Poisson equation')
ax.legend()

plt.show()
