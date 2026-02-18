cmake_minimum_required(VERSION 3.27)

project(gamma LANGUAGES CXX)

include(GNUInstallDirs)

set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_COLOR_DIAGNOSTICS ON)
set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)
set(CMAKE_SKIP_BUILD_RPATH FALSE)
set(CMAKE_BUILD_WITH_INSTALL_RPATH FALSE)
set(CMAKE_INSTALL_RPATH "$ORIGIN;$ORIGIN/${CMAKE_INSTALL_LIBDIR}")
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH FALSE)
set(CMAKE_INSTALL_BINDIR .)

find_package(test_beta REQUIRED)

install(RUNTIME_DEPENDENCY_SET my_app_deps
	DESTINATION .
	PRE_EXCLUDE_REGEXES
		[=[api-ms-]=] # VC Redistibutable DLLs
		[=[ext-ms-]=] # Windows extension DLLs
		# [=[python]=]
		[[kernel32\.dll]] # Default in conan doc
		[[libc\.so\..*]] [[libgcc_s\.so\..*]] [[libm\.so\..*]] [[libstdc\+\+\.so\..*]] # Default in conan doc
	POST_EXCLUDE_REGEXES
		[=[.*system32\/.*\.dll]=] # Windows system DLLs
		[=[^\/(lib*|usr\/lib*|usr\/local\/lib*\/lib64)]=] # Unix system libraries
	DIRECTORIES
		${CONAN_RUNTIME_LIB_DIRS}
)

install(
	IMPORTED_RUNTIME_ARTIFACTS
		Beta::beta
	RUNTIME_DEPENDENCY_SET
		my_app_deps
	DESTINATION .
)