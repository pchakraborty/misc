TMPFILEBASE = 'intermediate'

module = '''
from {} import ffi
import fort2py as f2p
from loop import march_in_time

@ffi.def_extern()
def march_in_time_interface(nx, ny, nz, origin_ptr, infld_ptr, outfld_ptr, dim_ptr):
    dim = f2p.fort2numpy(ffi, dim_ptr, (3,))
    origin = f2p.fort2numpy(ffi, origin_ptr, (3,))
    backend = 'gtx86'
    in_field = f2p.fort2gt4py(ffi, infld_ptr, dim, origin, backend)
    out_field = f2p.fort2gt4py(ffi, outfld_ptr, dim, origin, backend)
    march_in_time(nx, ny, nz, origin, in_field, out_field)
'''.format(TMPFILEBASE)

import cffi
ffibuilder = cffi.FFI()

header = 'extern void march_in_time_interface(int, int, int, int *, double *, double *, int *);'
with open(TMPFILEBASE+'.h', 'w') as f:
    f.write(header)
ffibuilder.embedding_api(header)
ffibuilder.set_source(TMPFILEBASE, r'''
    #include "{}.h"
'''.format(TMPFILEBASE))
ffibuilder.embedding_init_code(module)
ffibuilder.compile(target='lib'+TMPFILEBASE+'.so', verbose=True)
