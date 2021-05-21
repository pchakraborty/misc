import numpy as np
from collections import namedtuple

import gt4py
from stencil import double_laplacian, euler_step, time_swap
from tools.plotting import plot_two_ij_slices

Geometry = namedtuple('Geometry', ['nx', 'ny', 'nz', 'nhalo', 'origin'])

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

if __name__ == '__main__':

    halo_size = 3
    geometry = Geometry(
        nx = 8, ny = 8, nz = 1,
        nhalo = halo_size,
        origin = (halo_size, halo_size, 0)
    )
    backend = 'numpy'
    
    in_field, out_field = get_inout_fields(backend, geometry)
    print(in_field[:,:,0])
    orig_field = in_field.copy()

    # run stencil
    alpha = 1./32.
    origin = geometry.origin
    domain = (geometry.nx, geometry.ny, geometry.nz)
    for n in range(20):
        double_laplacian(in_field=in_field, out_field=out_field, origin=origin, domain=domain)
        euler_step(in_field=in_field, out_field=out_field, alpha=alpha, origin=origin, domain=domain)
        time_swap(in_field=in_field, out_field=out_field, origin=origin, domain=domain)

    # plot
    plot_two_ij_slices(orig_field, out_field)
