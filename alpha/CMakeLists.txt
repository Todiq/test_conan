cmake_minimum_required(VERSION 3.27)

project(test LANGUAGES CXX)

include(GNUInstallDirs)

set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_COLOR_DIAGNOSTICS ON)
set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)
set(CMAKE_SKIP_BUILD_RPATH FALSE)
set(CMAKE_BUILD_WITH_INSTALL_RPATH FALSE)
set(CMAKE_INSTALL_RPATH "$ORIGIN;$ORIGIN/${CMAKE_INSTALL_LIBDIR}")
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)
set(CMAKE_INSTALL_BINDIR .)

if (WIN32)
	add_compile_options(-D_AFXDLL)
	add_compile_options(-D_SBCS)
	add_compile_options(-D_WIN32_WINNT=0x0A00)
	add_compile_options(/W3)
endif()

find_package(ZLIB QUIET)

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
		src/alpha.cpp
)

target_link_libraries(${PROJECT_NAME}
	PUBLIC
		Alpha::headers
		ZLIB::ZLIB
)

install(TARGETS ${PROJECT_NAME}
	RUNTIME_DEPENDENCY_SET my_app_deps
	DESTINATION ${DEPS_DESTINATION}
)

install(RUNTIME_DEPENDENCY_SET my_app_deps
	PRE_EXCLUDE_REGEXES
		[=[api-ms-]=] # VC Redistibutable DLLs
		[=[ext-ms-]=] # Windows extension DLLs
		[[kernel32\.dll]] # Default in conan doc
		[[libc\.so\..*]] [[libgcc_s\.so\..*]] [[libm\.so\..*]] [[libstdc\+\+\.so\..*]] # Default in conan doc
	POST_EXCLUDE_REGEXES
		[=[.*system32\/.*\.dll]=] # Windows system DLLs
		[=[^\/(lib|usr\/lib|usr\/local\/lib)]=] # Unix system libraries
	DIRECTORIES ${CONAN_RUNTIME_LIB_DIRS}
)