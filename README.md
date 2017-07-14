HDF5 take 2: h5py & PyTables
============================

Introduction
------------

Here are the materials for the Scipy 2017 tutorial on Monday, July 10th.

You can get the latest release of the materials here:

<https://github.com/tomkooij/scipy2017/releases>

Or clone this repo:

    > git clone https://github.com/tomkooij/scipy2017

Installation
------------

Make sure that you have the following Python packages installed:

-   python 3
-   jupyter
-   NumPy
-   h5py
-   PyTables
-   pandas
-   matplotlib
-   cartopy

For (ana)conda users an enviroment (called hdf5) with all required packages can be created using the provided environment.yml. On windows:

    > conda env create -f environment-windows.yml

Activate the environment with:

    > activate hdf5

Or Linux/Mac:

    $ conda env create -f environment.yml
    $ source activate hdf5

Now run the test script:

    > python test_env.py

Verify the jupyter notebook server works:

    > jupyter notebook

And run the 'test\_env.ipynb' notebook.

Python 3
--------

The notebooks are written and testing on python 3 only. Using python 2.7 is possible but not recommended.

Optional HDF5 1.10 enviroment (Linux/Mac only)
----------------------------------------------

For notebook 10 (Parallel HDF5) h5py built against HDF5 v1.10 is needed with and without Parallel HDF5 enabled. More on this in the tutorial.

If possible create a (python 2.7!) enviroment with HDF5 1.10 and h5py:

    $ conda create -n hdf5_1-10 python=2.7
    $ source activate hdf5_1-10
    $ conda install -c cfel hdf5 h5py

And for Parallel HDF5 and h5py:

    $ conda create -n hdf5-mpi python=2.7
    $ source activate hdf5_1-10
    $ conda install -c cfel hdf5-mpi h5py-mpi mpi4py

Description
-----------

HDF5 is a hierarchical, binary database format that has become the de facto standard for scientific computing. While the specification may be used in a relatively simple way (persistence of static arrays) it also supports several high-level features that prove invaluable. These include chunking, ragged data, extensible data, parallel I/O, compression, complex selection, and in-core calculations. Moreover, HDF5 bindings exist for almost every language - including two Python libraries (PyTables and h5py). This tutorial will cover HDF5 itself through the lens of both h5py and PyTables and will show how to use them in order to persist NumPy and pandas containers.

Outline
-------

Part One:

> -   Introduction (15 min)
> -   Notebook 1 Using the hierarchy
> -   Notebook 2 Advanced datatypes
>     -   Homogeneous types (Arrays)
>     -   Compound types (Tables)
>     -   Nested types
> -   Exercise on above topics

Part Two:

> -   Notebook 3 Chunking
>     -   How it works
>     -   How to properly select your chunksize
>     -   Exercise
> -   The Starving CPU Problem
>     -   Why you should always use compression
>     -   Compression algorithms available
>     -   Choosing the correct one
> -   Notebook 4 Compression
>     -   Exercise

Part Three:

> -   Notebook 5 Queries and Selections (PyTables)
>     -   PyTables.where()
>     -   In-core vs Out-of-core
>     -   Normalized vs Denormalized tables
> -   Notebook 6 Indexing
> -   Notebook 7 Expressions
>
>     > -   In-core vs Out-of-core
>
Part Four:

> -   Notebook 8 Integration with pandas (HDFStore)
>     -   Storing/loading dataframes
>     -   Querying a serialised dataframe
>     -   Creating indexes for improved query times
>     -   Exercise

Part Five:

> -   Notebook 9 Low Level API (h5py)
> -   Notebook 10 Parallel HDF5
>     -   Thread-safe vs Parallel HDF5
>     -   Parallel HDF5 using MPI
>     -   SMWR in HDF5 1.10

[![Video registration of the tutorial](https://img.youtube.com/vi/ofLFhQ9yxCw&t/0.jpg)](https://www.youtube.com/watch?v=ofLFhQ9yxCw&t)
