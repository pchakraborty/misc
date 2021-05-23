import numpy as np
from geometry import Geometry

import gt4py

def get_inout_fields(backend, geometry, datatype=np.float64):
    nx, ny, nz, nhalo, origin = geometry
    shape = (nx + 2*nhalo, ny + 2*nhalo, nz)
    in_field = gt4py.storage.zeros(backend, origin, shape, datatype)
    for k in range(nz):
        for j in range(nhalo, ny+nhalo):
            for i in range(nhalo, nx+nhalo):
                in_field[i,j,k] = (i + j + k) % 4
    out_field = gt4py.storage.zeros(backend, origin, shape, datatype)
    return (in_field, out_field)
