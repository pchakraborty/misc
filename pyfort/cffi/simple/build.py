module = '''
from tmplib import ffi
import python_function

@ffi.def_extern()
def do_something_wrapper():
    python_function.do_something()
'''

import cffi
ffibuilder = cffi.FFI()

header = 'extern void do_something_wrapper(void);'
with open('tmplib.h', 'w') as f:
    f.write(header)
ffibuilder.embedding_api(header)
ffibuilder.set_source('tmplib', r'''
    #include "tmplib.h"
''')
ffibuilder.embedding_init_code(module)
ffibuilder.compile(target='libpyfunc.so', verbose=True)
