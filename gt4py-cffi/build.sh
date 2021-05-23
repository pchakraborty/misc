python ffibuilder.py
gfortran -L./ -lintermediate geometry.f90 initialize.f90 pyfortinterface.f90 main.f90
