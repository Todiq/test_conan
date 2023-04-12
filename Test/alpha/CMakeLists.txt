cmake_minimum_required(VERSION 3.15)
project(myalpha LANGUAGES CXX)

set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_CXX_STANDARD 17)

add_library(alpha INTERFACE)

target_include_directories(alpha
	INTERFACE
		${CMAKE_CURRENT_SOURCE_DIR}/include
)

add_subdirectory(alpha1/alpha1_1)
add_subdirectory(alpha1/alpha1_2)
add_subdirectory(alpha2)

install(TARGETS alpha alpha1_1 alpha1_2 alpha2)