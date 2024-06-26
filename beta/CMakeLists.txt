cmake_minimum_required(VERSION 3.29)

project(beta LANGUAGES CXX)

include(GNUInstallDirs)

set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_COLOR_DIAGNOSTICS ON)
# set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)
set(CMAKE_SKIP_BUILD_RPATH FALSE)
set(CMAKE_BUILD_WITH_INSTALL_RPATH FALSE)
set(CMAKE_INSTALL_RPATH "$ORIGIN;$ORIGIN/${CMAKE_INSTALL_LIBDIR};$ORIGIN/${CMAKE_INSTALL_LIBEXECDIR}")
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)

if (WIN32)
	add_compile_options(-D_AFXDLL)
	add_compile_options(-D_SBCS)
    add_compile_options(-DBOOST_USE_WINAPI_VERSION=BOOST_WINAPI_VERSION_WIN7)
	add_compile_options(-DBOOST_LOG_DYN_LINK)
	add_compile_options(-D_WIN32_WINNT=0x0A00)
	add_compile_options(/W3)
endif()

find_package(alpha QUIET)

add_executable(${PROJECT_NAME})

target_sources(${PROJECT_NAME}
	PRIVATE
		src/beta.cpp
)

target_link_libraries(${PROJECT_NAME}
	PRIVATE
        Alpha::hello
)

install(TARGETS ${PROJECT_NAME} RUNTIME_DEPENDENCY_SET my_app_deps)

install(RUNTIME_DEPENDENCY_SET my_app_deps
	PRE_EXCLUDE_REGEXES
		[=[api-ms-]=]
		[=[ext-ms-]=]
		[[kernel32\.dll]]
		[[libc\.so\..*]] [[libgcc_s\.so\..*]] [[libm\.so\..*]] [[libstdc\+\+\.so\..*]]
	POST_EXCLUDE_REGEXES
		[=[.*system32\/.*\.dll]=]
		[=[^\/(lib|usr\/lib|usr\/local\/lib)]=]
	DIRECTORIES ${CONAN_RUNTIME_LIB_DIRS}
)