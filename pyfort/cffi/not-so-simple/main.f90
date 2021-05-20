program main

  use, intrinsic :: iso_c_binding

  implicit none

  interface
     subroutine print_array_1dr4_wrapper(arr1dr4, len) bind(c)
       use iso_c_binding
       integer(c_int), value :: len
       real(c_float) :: arr1dr4(len)
     end subroutine print_array_1dr4_wrapper
  end interface

  integer, parameter :: LENGTH = 10
  real :: myarr(LENGTH)
  real, allocatable :: myarralloc(:)
  integer :: ctr

  do ctr = 1, LENGTH
     myarr(ctr) = ctr
  end do
  print *, 'Fortran array:', myarr
  call print_array_1dr4_wrapper(myarr, LENGTH)

  allocate(myarralloc(LENGTH), source=myarr)
  call print_array_1dr4_wrapper(myarralloc, LENGTH)
  
end program main
