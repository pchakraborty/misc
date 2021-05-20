import numpy as np

TYPEMAP = dict()
TYPEMAP['float'] = np.dtype('f4')

def fort2py_1dr4(ffi, fptr, length):
    ftype = ffi.getctype(ffi.typeof(fptr).item)
    assert ftype=='float'
    dtype = np.dtype('f4')
    return np.frombuffer(ffi.buffer(fptr, length*ffi.sizeof(ftype)), dtype)
