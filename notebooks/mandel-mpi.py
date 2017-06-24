from __future__ import print_function

from mpi4py import MPI

import numpy as np
import h5py

SIZE = 10

mpi_size = MPI.COMM_WORLD.size
mpi_rank = MPI.COMM_WORLD.rank

print("I am worker: %d of %d" % (mpi_rank, mpi_size))


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

f = h5py.File('mandel.h5', 'w', driver='mpio', comm=MPI.COMM_WORLD)
dset = f.create_dataset('/m', shape=(SIZE, SIZE), dtype='i')
dset.attrs['size'] = SIZE


# create a list of rows, split it into the number of workers.
rows = np.arange(SIZE)
my_rows = np.array_split(rows, mpi_size)[mpi_rank]

for row, y in enumerate(list(Y)):
    if row not in my_rows:
	continue
    print ("worker %d row %d of %d" % (mpi_rank, row, SIZE))
    for col, x in enumerate(X):
        Z[col] = mandelbrot(x + 1j * y)
    dset[row] = Z
    f.flush()

f.close()
