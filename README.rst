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

Make the jupyter notebook server works:

   > jupyter notebooks

And run the 'test_environment.ipynb' notebook.



Description
-----------

HDF5 is a hierarchical, binary database format that has become the de facto standard for scientific computing. While the specification may be used in a relatively simple way (persistence of static arrays) it also supports several high-level features that prove invaluable. These include chunking, ragged data, extensible data, parallel I/O, compression, complex selection, and in-core calculations. Moreover, HDF5 bindings exist for almost every language - including two Python libraries (PyTables and h5py). This tutorial will cover HDF5 itself through the lens of both h5py and PyTables and will show how to use them in order to persist NumPy and pandas containers.

This tutorial will discuss tools, strategies, and hacks for really squeezing every ounce of performance out of HDF5 in new or existing projects. It will also go over fundamental limitations in the specification and provide creative and subtle strategies for getting around them. We will also see how pandas can use HDF5 via its HDFStore module.  Overall, this tutorial will show how HDF5 plays nicely with all parts of an application making the code and data both faster and smaller.

Knowledge of Python, NumPy, pandas, C or C++, and basic HDF5 is recommended but not required.

Outline
-------

Part One:

 - Meaning in layout (h5py) (20 min)

   - Tips for choosing your hierarchy

 - Advanced datatypes (20 min)

   - Homogeneous types (Arrays)
   - Compound types (Tables)
   - Nested types

 - Exercise on above topics (20 min)

Part Two:

 - h5py advanced features (20 min)

   - Parallelism, modern format, low level API

 - Exercises on above topics (20 min)

Part Three:

 - Chunking (20 min)

   - How it works
   - How to properly select your chunksize
 - Queries and Selections (PyTables) (20 min)

   - In-core vs Out-of-core calculations
   - PyTables.where()
   - Datasets vs Dataspaces
 - Exercise on above topics (20 min)

Part Four:

 - The Starving CPU Problem (40 min)

   - Why you should always use compression
   - Compression algorithms available
   - Choosing the correct one
 - Exercise

Part Five:

  - Integration with pandas (HDFStore) (40 min)

    - Storing/loading dataframes
    - Querying a serialised dataframe
    - Creating indexes for improved query times
  - Performance tricks
  - Exercise
​
