cmake_minimum_required(VERSION 3.15)
project(headers LANGUAGES CXX)

set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_CXX_STANDARD 17)

add_library(${PROJECT_NAME} INTERFACE)

target_include_directories(${PROJECT_NAME}
	INTERFACE
		${CMAKE_CURRENT_SOURCE_DIR}/include
)

add_subdirectory(alpha1/alpha1_1)
add_subdirectory(alpha1/alpha1_2)
add_subdirectory(alpha2)

install(TARGETS ${PROJECT_NAME} alpha1_1 alpha1_2 alpha2)

install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/Alpha
		TYPE INCLUDE
)