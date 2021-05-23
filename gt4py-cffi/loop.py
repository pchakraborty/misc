from stencil import double_laplacian, euler_step, time_swap
from tools.plotting import plot_two_ij_slices

def march_in_time(nx, ny, nz, ox, oy, oz, in_field, out_field):
    orig_field = in_field.copy()
    alpha = 1./32.
    domain = (nx, ny, nz)
    origin = (ox, oy, oz)
    for n in range(20):
        double_laplacian(in_field=in_field, out_field=out_field, origin=origin, domain=domain)
        euler_step(in_field=in_field, out_field=out_field, alpha=alpha, origin=origin, domain=domain)
        time_swap(in_field=in_field, out_field=out_field, origin=origin, domain=domain)
    plot_two_ij_slices(orig_field, out_field)
    return out_field
