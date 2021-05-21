import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import gt4py
from gt4py import gtscript
from gt4py.gtscript import Field

from tools.plotting import plot_two_ij_slices

@gtscript.function
def laplacian(in_field: Field[np.float64], coeff: np.float64 = 1.0):
    return coeff * (
        - 4 * in_field
        +     in_field[-1, 0, 0]
        +     in_field[+1, 0, 0]
        +     in_field[ 0,-1, 0]
        +     in_field[ 0,+1, 0] )

backend = 'gtx86'

@gtscript.stencil(backend=backend)
def double_laplacian(
        in_field: Field[np.float64],
        out_field: Field[np.float64],
        coeff: np.float64 = 1.0):
    with computation(PARALLEL), interval(...):
        tmp_field = laplacian(in_field, coeff)
        out_field = laplacian(tmp_field, coeff)

@gtscript.stencil(backend=backend)
def euler_step(
        in_field: Field[np.float64],
        out_field: Field[np.float64],
        *,
        alpha: np.float64):
    with computation(PARALLEL), interval(...):
        out_field = in_field - alpha * out_field

@gtscript.stencil(backend=backend)
def time_swap(in_field: Field[np.float64], out_field: Field[np.float64]):
    with computation(PARALLEL), interval(...):
        in_field = out_field

# storage
nhalo = 3
nx, ny, nz = 8, 8, 1
origin = (nhalo, nhalo, 0)
domain = (nx, ny, nz)
shape = (nx + 2*nhalo, ny + 2*nhalo, nz)
in_field = gt4py.storage.zeros(backend, origin, shape, dtype=np.float64)
for k in range(nz):
    for j in range(nhalo, ny+nhalo):
        for i in range(nhalo, nx+nhalo):
            in_field[i,j,k] = (i + j + k) % 4
orig_field = in_field.copy()
out_field = gt4py.storage.zeros(backend, origin, shape, dtype=np.float64)
print(orig_field[:,:,0])
np.savetxt('orig-field.csv', orig_field[:,:,0], delimiter=',')

# run stencil
alpha = 1./32.
for n in range(20):
    double_laplacian(in_field=in_field, out_field=out_field, origin=origin, domain=domain)
    euler_step(in_field=in_field, out_field=out_field, alpha=alpha, origin=origin, domain=domain)
    time_swap(in_field=in_field, out_field=out_field, origin=origin, domain=domain)

# plot
plot_two_ij_slices(orig_field, out_field)
