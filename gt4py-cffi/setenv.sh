source /discover/nobackup/pchakrab/code/venv/python3/gt4py/bin/activate
module load comp/gcc/9.3.0
export CPLUS_INCLUDE_PATH=/discover/nobackup/pchakrab/sw/boost_1_76_0
export PYTHONPATH=$PYTHONPATH:$(pwd)
export LD_LIBRARY_PATH=$(pwd):$LD_LIBRARY_PATH
