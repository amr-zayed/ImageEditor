import ctypes
from ctypes import *
import sys
import pathlib
from numpy.ctypeslib import ndpointer
import numpy as  np

# from test import do_square_using_c
# my_list = np.arange(1000)
# squared_list = do_square_using_c(*my_list)

lib_path = 'DFT_%s.so' % (sys.platform)
basic_function_lib = CDLL(lib_path)
print((basic_function_lib,lib_path))
python_c_DFT = basic_function_lib.DFT
python_c_DFT.restype = None
#python_c_DFT.restype = ndpointer(dtype=c_double, shape=(size,))

def c_DFT(signal):
    """Call C function to calculate squares"""
    print("2")
    size = len(signal)
    print("3")
    real = (c_double * size)(*signal)
    print("4")
    img = (c_double * size)()
    print("5")
    print("kfayaaaa")
    basic_function_lib.DFT(c_int(size), signal.ctypes.data_as(c_void_p), img)
    print("6")

    return  img[:]

Try_signal=np.array([0.0, 3219.0, 3035.0, 3346.0, 1006.0, 1797.0, 2456.0 , 1307.0 ])
print("1")
I=c_DFT(Try_signal)
print(I)

# print("hello")
# libname = pathlib.Path().absolute() / "DFT_win32.so"
# print("hey",libname)
# c_lib = ctypes.CDLL("D:/collage/theories/DFT_win32.so")
# python_c_DFT=c_lib.DFT
