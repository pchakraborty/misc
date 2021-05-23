import numpy as np

import gt4py
from geometry import Geometry
from initialize import get_inout_fields
from stencil import double_laplacian, euler_step, time_swap
from tools.plotting import plot_two_ij_slices
from mainloop import march_in_time

if __name__ == '__main__':

    halo_size = 3
    geometry = Geometry(
        nx = 8, ny = 8, nz = 1,
        nhalo = halo_size,
        origin = (halo_size, halo_size, 0)
    )
    backend = 'gtx86'
    
    in_field, out_field = get_inout_fields(backend, geometry)
    
    nx, ny, nz, _, (ox, oy, oz) = geometry
    out_field = march_in_time(nx, ny, nz, ox, oy, oz, in_field, out_field)
