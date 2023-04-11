set(PROJECT_NAME beta1_1)

project(${PROJECT_NAME} LANGUAGES CXX)

find_package(alpha)
find_package(ZLIB)

add_library(${PROJECT_NAME} SHARED)
add_library(beta::${PROJECT_NAME} ALIAS ${PROJECT_NAME})

target_sources(${PROJECT_NAME}
	PRIVATE
		src/beta1_1.cpp
)

target_include_directories(${PROJECT_NAME}
	PUBLIC
		${CMAKE_CURRENT_SOURCE_DIR}/include
	PRIVATE
		${CMAKE_CURRENT_SOURCE_DIR}/src
)

target_link_libraries(${PROJECT_NAME}
	PUBLIC
		alpha::alpha
		ZLIB::ZLIB
	PRIVATE
		beta::beta
)

include(GNUInstallDirs)
install(TARGETS ${PROJECT_NAME}
		ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
		LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
		RUNTIME DESTINATION ${CMAKE_INSTALL_LIBEXECDIR}
)
install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/beta1_1 TYPE INCLUDE)