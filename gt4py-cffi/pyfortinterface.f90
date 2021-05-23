module PythonFortranInterface

  implicit none

  private
  public :: march_in_time_wrapper
  
  interface
     subroutine march_in_time_wrapper( &
          nx, ny, nz, &
          ox, oy, oz, & ! origin
          in_field, out_field, &
          dim1, dim2, dim3 & ! dimensions of in/out fields
          ) bind(c)
       use iso_c_binding, only: c_int, c_double
       integer(c_int), value, intent(in) :: nx, ny, nz
       integer(c_int), value, intent(in) :: ox, oy, oz
       integer(c_int), value, intent(in) :: dim1, dim2, dim3
       real(c_double), intent(in) :: in_field(dim1, dim2, dim3)
       real(c_double), intent(out) :: out_field(dim1, dim2, dim3)
     end subroutine march_in_time_wrapper
  end interface
  
end module PythonFortranInterface
