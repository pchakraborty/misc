program main

  use iso_fortran_env, only: real64
  use Geometry, only: Geometry_T
  use Initialize, only: get_inout_fields
  use PythonFortranInterface, only: march_in_time_wrapper
  
  implicit none
  
  integer, parameter :: halo_size = 3
  type(Geometry_T) :: geometry
  real(real64), allocatable :: in_field(:,:,:)
  real(real64), allocatable :: out_field(:,:,:)
  integer :: dim(3)

  geometry = Geometry_T( &
       nx = 8, ny = 8, nz = 1, &
       nhalo = halo_size, &
       origin = [halo_size, halo_size, 0] &
       )

  call get_inout_fields(geometry, in_field, out_field, dim)
  call march_in_time_wrapper( &
       geometry%nx, geometry%ny, geometry%nz, &
       geometry%origin(1), geometry%origin(2), geometry%origin(3), & ! origin
       in_field, out_field, &
       dim(1), dim(2), dim(3) & ! dimensions of in/out fields
       )
  
end program main