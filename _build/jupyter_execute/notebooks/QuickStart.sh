create_newcase --case ~/b.e21_test1 --compset B1850 --res f09_g17

cd ~/b.e21_test1
./xmlchange STOP_OPTION=ndays,STOP_N=3

./xmlquery STOP_OPTION,STOP_N

./case.setup

./case.build

./case.submit

./xmlchange CONTINUE_RUN=true,STOP_N=28

./case.submit
