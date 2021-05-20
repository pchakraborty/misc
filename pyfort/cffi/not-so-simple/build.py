TMPFILEBASE = 'tmp'

module = '''
from {} import ffi
import pyfunc
import convert

@ffi.def_extern()
def print_array_1dr4_wrapper(fptr, length):
    nparr = convert.fort2py_1dr4(ffi, fptr, length)
    pyfunc.print_array(nparr)
'''.format(TMPFILEBASE)

import cffi
ffibuilder = cffi.FFI()

header = 'extern void print_array_1dr4_wrapper(float *, int);'
with open(TMPFILEBASE+'.h', 'w') as f:
    f.write(header)
ffibuilder.embedding_api(header)
ffibuilder.set_source(TMPFILEBASE, r'''
    #include "{}.h"
'''.format(TMPFILEBASE))
ffibuilder.embedding_init_code(module)
ffibuilder.compile(target='lib'+TMPFILEBASE+'.so', verbose=True)
