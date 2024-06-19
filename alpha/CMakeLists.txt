cmake_minimum_required(VERSION 3.29)

project(hello LANGUAGES CXX)

include(GNUInstallDirs)

set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_COLOR_DIAGNOSTICS ON)
set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)
set(CMAKE_SKIP_BUILD_RPATH FALSE)
set(CMAKE_BUILD_WITH_INSTALL_RPATH FALSE)
set(CMAKE_INSTALL_RPATH "$ORIGIN;$ORIGIN/${CMAKE_INSTALL_LIBDIR};$ORIGIN/${CMAKE_INSTALL_LIBEXECDIR}")
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)

if (WIN32)
	add_compile_options(-D_AFXDLL)
	add_compile_options(-D_SBCS)
	add_compile_options(-D_WIN32_WINNT=0x0A00)
	add_compile_options(/W3)
endif()

find_package(Boost QUIET)
find_package(Python COMPONENTS Development QUIET)

# Global include folder
add_library(headers INTERFACE)
add_library(Alpha::headers ALIAS headers)

target_include_directories(headers
	INTERFACE
		${CMAKE_CURRENT_SOURCE_DIR}/include
)

install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/alpha
		TYPE INCLUDE
)

# Library

add_library(${PROJECT_NAME})
add_library(Alpha::${PROJECT_NAME} ALIAS ${PROJECT_NAME})

target_sources(${PROJECT_NAME}
	PRIVATE
		src/hello.cpp
)

target_link_libraries(${PROJECT_NAME}
	PUBLIC
		Alpha::headers
		Boost::python
		Python::Python
)

install(TARGETS ${PROJECT_NAME})