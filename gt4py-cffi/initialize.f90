module Initialize

  use iso_fortran_env, only: real64
  use Geometry, only: Geometry_T

  implicit none

  private
  public :: get_inout_fields
  
contains

  subroutine get_inout_fields(geometry, in_field, out_field, dim)

    ! Arguments
    type(Geometry_T), intent(in) :: geometry
    real(real64), allocatable, intent(out) :: in_field(:,:,:)
    real(real64), allocatable, intent(out) :: out_field(:,:,:)
    integer, intent(out) :: dim(3)

    ! Locals
    integer :: i, j, k, nhalo

    ! Start here
    nhalo = geometry%nhalo
    dim(1) = geometry%nz
    dim(2) = geometry%ny + 2 * nhalo
    dim(3) = geometry%nx + 2 * nhalo
    
    allocate(in_field(dim(1), dim(2), dim(3)), source=0.0_real64)
    allocate(out_field, mold=in_field)
    
    do i = nhalo+1, geometry%nx+nhalo
       do j = nhalo+1, geometry%ny+nhalo
          do  k = 1, geometry%nz
             ! in_field(1, j, i) = 10 * (j-geometry%nhalo) + (i-geometry%nhalo)
             in_field(k, j, i) = mod(i + j + k - 3, 4)
          end do
       end do
    end do

    ! write(*,"(*(g0))") ((in_field(1,j,i),"  ",i=1,dim(3)), new_line("A"), j=1,dim(2))
    ! print *, ''
    ! print *, in_field
    
  end subroutine get_inout_fields
  
end module Initialize
