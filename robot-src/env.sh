sudo sysctl -w net.core.rmem_max=30000000
export CYCLONEDDS_URI=file://$PWD/cyclonedds.xml
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
# export ROS_DOMAIN_ID=21
export PS1="🐳  \[\033[1;36m\]\h \[\033[1;34m\]\W\[\033[0;35m\] \[\033[1;36m\]# \[\033[0m\]"
source install/setup.bash
source aliases.sh


