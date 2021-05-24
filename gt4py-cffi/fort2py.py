import numpy as np
from math import prod

TYPEMAP = {
    'float': np.dtype('f4'),
    'double': np.dtype('f8'),
    'int': np.dtype('i4'),
}

def convert_arr(ffi, fptr, dim):
    ftype = ffi.getctype(ffi.typeof(fptr).item)
    assert ftype in TYPEMAP
    return np.frombuffer(
        ffi.buffer(fptr, prod(dim)*ffi.sizeof(ftype)),
        TYPEMAP[ftype],
    ).reshape(tuple(reversed(dim)))
