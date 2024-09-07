cmake_minimum_required(VERSION 3.8)
project(demos)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
set(NODES
  demos/sub_demo.py
  demos/pub_demo.py
  demos/service_demo.py
)

install(PROGRAMS
    ${NODES}

DESTINATION lib/${PROJECT_NAME}
)

# install(DIRECTORY
#   launch
#   DESTINATION share/${PROJECT_NAME}
# )


ament_package()
