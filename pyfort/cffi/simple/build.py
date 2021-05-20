TMPFILEBASE = 'intermediate'

module = '''
from {} import ffi
import pyfunc

@ffi.def_extern()
def do_something_wrapper():
    pyfunc.do_something()
'''.format(TMPFILEBASE)

import cffi
ffibuilder = cffi.FFI()

header = 'extern void do_something_wrapper(void);'
with open(TMPFILEBASE+'.h', 'w') as f:
    f.write(header)
ffibuilder.embedding_api(header)
ffibuilder.set_source(TMPFILEBASE, r'''
    #include "{}.h"
'''.format(TMPFILEBASE))
ffibuilder.embedding_init_code(module)
ffibuilder.compile(target='lib'+TMPFILEBASE+'.so', verbose=True)
