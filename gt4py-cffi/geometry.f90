module Geometry

  implicit none

  private
  public :: Geometry_T
  
  type Geometry_T
     integer :: nx, ny, nz
     integer :: nhalo
     integer :: origin(3)
  end type Geometry_T

end module Geometry
