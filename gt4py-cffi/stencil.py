import numpy as np

import gt4py
from gt4py import gtscript
from gt4py.gtscript import Field

backend = 'gtx86'

@gtscript.function
def laplacian(in_field: Field[np.float64], coeff: np.float64 = 1.0):
    return coeff * (
        - 4 * in_field
        +     in_field[-1, 0, 0]
        +     in_field[+1, 0, 0]
        +     in_field[ 0,-1, 0]
        +     in_field[ 0,+1, 0] )

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
