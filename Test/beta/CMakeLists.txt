cmake_minimum_required(VERSION 3.23)

set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_CXX_STANDARD 17)
set(PROJECT_NAME beta)

project(${PROJECT_NAME} LANGUAGES CXX)

add_library(${PROJECT_NAME} INTERFACE)
add_library(beta::${PROJECT_NAME} ALIAS ${PROJECT_NAME})

target_include_directories(${PROJECT_NAME}
	INTERFACE
		${CMAKE_CURRENT_SOURCE_DIR}/include
)
install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/beta TYPE INCLUDE)

add_subdirectory(beta1)
#add_subdirectory(beta2)