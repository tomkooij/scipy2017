HDF5 take 2: h5py & PyTables (Intermediate/Advanced)
====================================================

Introduction
------------

Here are my materials for the tutorial on Monday, July 10th, Scipy 2017.

You can get the latest release of the materials here:

https://github.com/tomkooij/scipy2017/releases (WIP)

Also, make sure that you have the next Python packages installed:

* jupyter
* NumPy
* h5py
* PyTables
* pandas
* matplotlib
* cartopy

For (ana)conda users an enviroment (called hdf5) with all required packages
can be created using the provided environment.yml. On windows::

   > conda env create -f environment-windows.yml

Activate the environment with::

   > activate hdf5

Or Linux/Mac::

   $ conda env create -f environment.yml
   $ source activate hdf5

Now run the test script::

   > python test_environment.py

Make the jupyter notebook server works::

   > jupyter notebooks

And run the 'test_environment.ipynb' notebook.

Optional HDF5 1.10 enviroment (Linux/Mac only)
----------------------------------------------

To follow along with the last part HDF5 v1.10 is needed with and without
Parallel HDF5 enabled. More on this in the tutorial. If possible create the
an (python 2.7!) enviroment with HDF5 1.10 and h5py::

    $ conda create -n hdf5_1-10 python=2.7
    $ source activate hdf5_1-10
    $ conda install -c cfel hdf5 h5py

And for Parallel HDF5 and h5py::

    $ conda create -n hdf5-mpi python=2.7
    $ source activate hdf5_1-10
    $ conda install -c cfel hdf5-mpi h5py-mpi mpi4py


Description
-----------

HDF5 is a hierarchical, binary database format that has become the de facto standard for scientific computing. While the specification may be used in a relatively simple way (persistence of static arrays) it also supports several high-level features that prove invaluable. These include chunking, ragged data, extensible data, parallel I/O, compression, complex selection, and in-core calculations. Moreover, HDF5 bindings exist for almost every language - including two Python libraries (PyTables and h5py). This tutorial will cover HDF5 itself through the lens of both h5py and PyTables and will show how to use them in order to persist NumPy and pandas containers.

This tutorial will discuss tools, strategies, and hacks for really squeezing every ounce of performance out of HDF5 in new or existing projects. It will also go over fundamental limitations in the specification and provide creative and subtle strategies for getting around them. We will also see how pandas can use HDF5 via its HDFStore module.  Overall, this tutorial will show how HDF5 plays nicely with all parts of an application making the code and data both faster and smaller.

Knowledge of Python, NumPy, pandas, C or C++, and basic HDF5 is recommended but not required.

Outline
-------

Part One:

 - Introduction (15 min)

 - Notebook 1 Using the hierarchy (10 min)
 - Notebook 2 Advanced datatypes (20 min)
   - Homogeneous types (Arrays)
   - Compound types (Tables)
   - Nested types
 - Exercise on above topics (20 min)

Part Two:

 - Notebook 3 Chunking (20 min)

   - How it works
   - How to properly select your chunksize
   - Exercise

 - The Starving CPU Problem (15 min)

   - Why you should always use compression
   - Compression algorithms available
   - Choosing the correct one

 - Notebook 4 Compression (20 min)
   - Exercise

Part Three:

- Notebook 5 Queries and Selections (PyTables) (20 min)
   - PyTables.where()
   - In-core vs Out-of-core
   - Normalized vs Denormalized tables

- Notebook 6 Indexing (15 min)
- Notebook 7 Expressions (15 min)
  - In-core vs Out-of-core

 - Exercise on above topics (20 min)

Part Four:

  - Notebook 8 Integration with pandas (HDFStore) (40 min)

    - Storing/loading dataframes
    - Querying a serialised dataframe
    - Creating indexes for improved query times
    - Performance tricks
    - Exercise
​
Part Five:

  - Notebook 9 Low Level API (h5py) (15 min)
  - Notebook 10 Parallel HDF5       (40 min)
    - Thread-safe vs Parallel HDF5
    - Parallel HDF5 using MPI
    - SMWR in HDF5 1.10
