# Install script for directory: /home/teamA/test/absl_ubuntu/all_ws/oriLimit_speed_ws/src/Reinforment_Implementation-on-a-Quadruped/quadruped_imu_and_servo/quadruped_imu_publisher

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/teamA/test/absl_ubuntu/all_ws/oriLimit_speed_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/teamA/test/absl_ubuntu/all_ws/oriLimit_speed_ws/build/Reinforment_Implementation-on-a-Quadruped/quadruped_imu_and_servo/quadruped_imu_publisher/catkin_generated/installspace/quadruped_imu_publisher.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/quadruped_imu_publisher/cmake" TYPE FILE FILES
    "/home/teamA/test/absl_ubuntu/all_ws/oriLimit_speed_ws/build/Reinforment_Implementation-on-a-Quadruped/quadruped_imu_and_servo/quadruped_imu_publisher/catkin_generated/installspace/quadruped_imu_publisherConfig.cmake"
    "/home/teamA/test/absl_ubuntu/all_ws/oriLimit_speed_ws/build/Reinforment_Implementation-on-a-Quadruped/quadruped_imu_and_servo/quadruped_imu_publisher/catkin_generated/installspace/quadruped_imu_publisherConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/quadruped_imu_publisher" TYPE FILE FILES "/home/teamA/test/absl_ubuntu/all_ws/oriLimit_speed_ws/src/Reinforment_Implementation-on-a-Quadruped/quadruped_imu_and_servo/quadruped_imu_publisher/package.xml")
endif()

