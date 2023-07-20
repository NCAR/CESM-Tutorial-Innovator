create_newcase --case case3 --compset B1850 --res f09_g17 

cd case3
./case.setup
 type physics_tend

     integer   ::   psetcols=0 ! max number of columns set- if subcols = pcols*psubcols, else = pcols

     real(r8), dimension(:,:),allocatable        :: dtdt, dudt, dvdt
     real(r8), dimension(:),  allocatable        :: flx_net
     real(r8), dimension(:),  allocatable        :: &
          te_tnd,  &! cumulative boundary flux of total energy
          tw_tnd    ! cumulative boundary flux of total water
  end type physics_tend

qcmd -- ./case.build 
Temperature = 90F -> 90.0000000000001F
echo "pertlim = 3e-13" >> user_nl_cam

./xmlchange STOP_OPTION=nmonths,STOP_N=1

./xmlquery STOP_OPTION,STOP_N

./case.submit

squeue -u $USER
