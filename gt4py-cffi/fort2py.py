import numpy as np

TYPEMAP = {
    'float': np.dtype('f4'),
    'double': np.dtype('f8'),
    'int': np.dtype('i4'),
}

def convert_1darr(ffi, fptr, dim1):
    ftype = ffi.getctype(ffi.typeof(fptr).item)
    assert ftype in TYPEMAP
    dtype = TYPEMAP[ftype]
    return np.frombuffer(ffi.buffer(fptr, dim1*ffi.sizeof(ftype)), dtype)
    
def convert_2darr(ffi, fptr, dim1, dim2):
    ftype = ffi.getctype(ffi.typeof(fptr).item)
    assert ftype in TYPEMAP
    return np.frombuffer(
        ffi.buffer(fptr, dim1*dim2*ffi.sizeof(ftype)),
        TYPEMAP[ftype],
    ).reshape((dim2, dim1))

def convert_3darr(ffi, fptr, dim1, dim2, dim3):
    ftype = ffi.getctype(ffi.typeof(fptr).item)
    assert ftype in TYPEMAP
    return np.frombuffer(
        ffi.buffer(fptr, dim1*dim2*dim3*ffi.sizeof(ftype)),
        TYPEMAP[ftype],
    ).reshape((dim3, dim2, dim1))
