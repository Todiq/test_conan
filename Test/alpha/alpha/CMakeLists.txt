cmake_minimum_required(VERSION 3.23)

set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_CXX_STANDARD 17)
set(PROJECT_NAME alpha)

project(${PROJECT_NAME} LANGUAGES CXX)

if (WIN32)
	add_definitions(-D_AFXDLL)
	add_definitions(-D_SBCS)
	add_definitions(-DBOOST_USE_WINAPI_VERSION=BOOST_WINAPI_VERSION_WIN7)
	add_compile_options(-DBOOST_LOG_DYN_LINK)
endif()

find_package(Boost)

add_library(${PROJECT_NAME} SHARED)
add_library(alpha::${PROJECT_NAME} ALIAS ${PROJECT_NAME})

target_sources(${PROJECT_NAME}
	PRIVATE
		alpha.cpp
)

target_include_directories(${PROJECT_NAME}
	PUBLIC
		${CMAKE_CURRENT_SOURCE_DIR}/alpha_include
)

target_link_libraries(${PROJECT_NAME}
	PUBLIC
		boost::boost
)

include(GNUInstallDirs)

install(TARGETS ${PROJECT_NAME}
		ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
		LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
		RUNTIME DESTINATION ${CMAKE_INSTALL_LIBEXECDIR}
)