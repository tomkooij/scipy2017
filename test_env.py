import sys

print("Checking python version:")
if sys.version_info < (3, 4):
    print('ERROR: These notebooks require python 3!')
else:
    print('OK: Python > 3.4 found. ')

requirements = {'h5py', 'tables', 'matplotlib', 'pandas', 'cartopy'}

import importlib
print('Checking installed packages: ')
for module in requirements:
    try:
        mod = importlib.import_module(module)
        print('OK: %s %s' % (module, mod.__version__))
    except:
        print('FAIL: %s not installed.' % module)
