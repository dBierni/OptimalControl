cmake_minimum_required(VERSION 3.10)
project(OptimalControl LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Eigen3 REQUIRED)

add_library(optimalcontrol
    src/InvertedPendulum.cpp
    src/LQR.cpp
)

target_include_directories(optimalcontrol
    PUBLIC
        ${PROJECT_SOURCE_DIR}/include
)

target_link_libraries(optimalcontrol
    PUBLIC
        Eigen3::Eigen
)

add_executable(lqr_pendulum src/main.cpp)
target_link_libraries(lqr_pendulum optimalcontrol)
