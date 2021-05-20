# Membuat Harmonograph dengan Python
import numpy as np
import matplotlib.pyplot as plt

# Parameter yang digunakan\n,
n = 1000000
t = np.logspace(np.log10(10),np.log10(500),n)

# Silakan merubah parameter ini,
A = [  2, 12, 2.8, 1.5 ]
d = [ .004, .001, .002, .0015 ]
f = [   3, 3, 4, 2.5 ]

# Membuat pasangan x dan y\n",
x = A[0]*np.sin(t*f[0])*np.exp(-d[0]*t) + A[1]*np.sin(t*f[1])*np.exp(-d[1]*t)
y = A[2]*np.sin(t*f[2])*np.exp(-d[2]*t) + A[3]*np.sin(t*f[3])*np.exp(-d[3]*t)


# Menampilkan plot nya\n",
plt.plot(x,y,'r',linewidth=.1)
plt.axis('off'),
plt.show()
