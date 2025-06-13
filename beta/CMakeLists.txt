cmake_minimum_required(VERSION 3.27)

project(beta LANGUAGES CXX)

include(GNUInstallDirs)

set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_COLOR_DIAGNOSTICS ON)
set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)
set(CMAKE_SKIP_BUILD_RPATH FALSE)
set(CMAKE_BUILD_WITH_INSTALL_RPATH FALSE)
set(CMAKE_INSTALL_RPATH "$ORIGIN;$ORIGIN/${CMAKE_INSTALL_LIBDIR}")
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH FALSE)
set(CMAKE_INSTALL_BINDIR .)

add_compile_options(
	"$<$<CXX_COMPILER_ID:MSVC>:/W4;/D_AFXDLL;/D_SBCS;/D_WIN32_WINNT=0x0A00>"
)

find_package(test_alpha REQUIRED)
find_package(Python3 REQUIRED)

install(
	IMPORTED_RUNTIME_ARTIFACTS
		Alpha::alpha
		Python3::Interpreter
	RUNTIME_DEPENDENCY_SET
		my_app_deps
)

install(RUNTIME_DEPENDENCY_SET my_app_deps
	PRE_EXCLUDE_REGEXES
		[=[api-ms-]=]
		[=[ext-ms-]=]
		[[kernel32\.dll]]
		[[libc\.so\..*]] [[libgcc_s\.so\..*]] [[libm\.so\..*]] [[libstdc\+\+\.so\..*]]
	POST_EXCLUDE_REGEXES
		[=[.*system32\/.*\.dll]=]
		# [=[^\/(lib|usr\/lib|usr\/local\/lib\/lib64)]=]
	DIRECTORIES
		${CONAN_RUNTIME_LIB_DIRS}
)