import numpy as np
from math import prod
import gt4py

TYPEMAP = {
    'float': np.dtype('f4'),
    'double': np.dtype('f8'),
    'int': np.dtype('i4'),
}

def fort2numpy(ffi, fptr, dim):
    ftype = ffi.getctype(ffi.typeof(fptr).item)
    assert ftype in TYPEMAP
    return np.frombuffer(
        ffi.buffer(fptr, prod(dim)*ffi.sizeof(ftype)),
        TYPEMAP[ftype],
    ).reshape(tuple(reversed(dim)))

def fort2gt4py(ffi, fptr, dim, origin, backend):
    nparr = fort2numpy(ffi, fptr, dim)
    return gt4py.storage.wrap_cpu_array(nparr, backend, origin)
