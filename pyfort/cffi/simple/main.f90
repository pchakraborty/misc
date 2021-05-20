program main

  use, intrinsic :: iso_c_binding

  implicit none

  interface

     subroutine do_something_wrapper() bind(c)
     end subroutine do_something_wrapper

  end interface

  call do_something_wrapper()

end program main
