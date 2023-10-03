cmake_minimum_required(VERSION 3.15)

set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_SKIP_BUILD_RPATH TRUE) # Mimick Windows behaviour

option(BUILD_SHARED_LIBS "Build shared libraries (.dll/.so) instead of static ones (.lib/.a)" ON)

project(headers LANGUAGES CXX)

add_library(${PROJECT_NAME} INTERFACE)

target_include_directories(${PROJECT_NAME}
	INTERFACE
		${CMAKE_CURRENT_SOURCE_DIR}/include
)

if (MSVC)
	add_compile_options(/W3)
endif()

include(GNUInstallDirs)

add_subdirectory(alpha1)
add_subdirectory(alpha2)

if (NOT BUILD_TESTING STREQUAL OFF)
	enable_testing()
	add_subdirectory(alpha_exe)
endif()

install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/Alpha
		TYPE INCLUDE
)