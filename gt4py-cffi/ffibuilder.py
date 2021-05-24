TMPFILEBASE = 'intermediate'

module = '''
from {} import ffi
import fort2py
from loop import march_in_time

@ffi.def_extern()
def march_in_time_interface(nx, ny, nz, ox, oy, oz, infld_ptr, outfld_ptr, dim1, dim2, dim3):
    in_field = fort2py.convert_3darr(ffi, infld_ptr, dim1, dim2, dim3)
    out_field = fort2py.convert_3darr(ffi, outfld_ptr, dim1, dim2, dim3)
    march_in_time(nx, ny, nz, ox, oy, oz, in_field, out_field)
'''.format(TMPFILEBASE)

import cffi
ffibuilder = cffi.FFI()

header = 'extern void march_in_time_interface(int, int, int, int, int, int, double *, double *, int, int, int);'
with open(TMPFILEBASE+'.h', 'w') as f:
    f.write(header)
ffibuilder.embedding_api(header)
ffibuilder.set_source(TMPFILEBASE, r'''
    #include "{}.h"
'''.format(TMPFILEBASE))
ffibuilder.embedding_init_code(module)
ffibuilder.compile(target='lib'+TMPFILEBASE+'.so', verbose=True)
