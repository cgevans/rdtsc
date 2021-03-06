import sys
import ctypes
import pkg_resources
import os

if sys.platform == 'darwin':
    sofile = 'rdtsc.dylib'
elif sys.platform == 'win32':
    sofile = 'rdtsc.dll'
else:
    sofile = 'rdtsc.so.1'

path = pkg_resources.resource_filename('rdtsc', os.path.join('..', 'lib', sofile))

so = ctypes.CDLL(path, use_errno=True)

get_cycles = so.get_cycles
get_cycles.argtypes = []
get_cycles.restype = ctypes.c_ulonglong
