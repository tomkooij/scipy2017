from __future__ import print_function

import numpy as np
import h5py

SIZE = 1000

def mandelbrot(a):
    """very slow mandelbrot calculation"""
    z = 0
    for n in range(1, 255):
        z = z**2 + a
        if abs(z) > 2:
            return n
    return n
 

X = np.linspace(-2, .5, SIZE)
Y = np.linspace(-1,  1, SIZE)
Z = np.zeros((SIZE,))

f = h5py.File('mandel.h5', 'w', libver='latest')
f.swmr_mode = True
dset = f.create_dataset('/m', shape=(0, SIZE), dtype='i', maxshape=(None, SIZE))
dset.attrs['size'] = SIZE

for row, y in enumerate(Y):
    print (row, "of", len(Y))
    dset.resize(row+1, axis=0)
    for col, x in enumerate(X):
        Z[col] = mandelbrot(x + 1j * y)
    dset[row:] = Z
    f.flush()

f.close()
