cmake_minimum_required(VERSION 3.25)

set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_COLOR_DIAGNOSTICS ON)

project(ex LANGUAGES CXX)

option(BUILD_SHARED_LIBS "Build shared libraries (.dll/.so) instead of static ones (.lib/.a)" ON)

if (WIN32)
	macro(get_WIN32_WINNT version)
		if (CMAKE_SYSTEM_VERSION)
			set(ver ${CMAKE_SYSTEM_VERSION})
			string(REGEX MATCH "^([0-9]+).([0-9])" ver ${ver})
			string(REGEX MATCH "^([0-9]+)" verMajor ${ver})
			# Check for Windows 10, b/c we'll need to convert to hex 'A'.
			if("${verMajor}" MATCHES "10")
				set(verMajor "A")
				string(REGEX REPLACE "^([0-9]+)" ${verMajor} ver ${ver})
			endif()
			# Remove all remaining '.' characters.
			string(REPLACE "." "" ver ${ver})
			# Prepend each digit with a zero.
			string(REGEX REPLACE "([0-9A-Z])" "0\\1" ver ${ver})
			set(${version} "0x${ver}")
		endif()
	endmacro()
endif()

if (MSVC)
	get_WIN32_WINNT(ver)
	add_compile_options(-D_WIN32_WINNT=${ver})
endif()

add_subdirectory(src)

if (NOT BUILD_TESTING STREQUAL OFF)
	message("Compiling tests")
	enable_testing()
	add_subdirectory(tests)
endif()
