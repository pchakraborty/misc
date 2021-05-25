module PythonFortranInterface

  implicit none

  private
  public :: march_in_time_interface
  
  interface
     subroutine march_in_time_interface( &
          nx, ny, nz, &
          origin, &
          in_field, out_field, &
          dim & ! dimensions of in/out fields
          ) bind(c)
       use iso_c_binding, only: c_int, c_double
       integer(c_int), value, intent(in) :: nx, ny, nz
       integer(c_int), intent(in) :: origin(3)
       integer(c_int), intent(in) :: dim(3)
       real(c_double), intent(in) :: in_field(dim(1), dim(2), dim(3))
       real(c_double), intent(in) :: out_field(dim(1), dim(2), dim(3))
     end subroutine march_in_time_interface
  end interface

end module PythonFortranInterface
