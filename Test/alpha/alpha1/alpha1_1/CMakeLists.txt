project(alpha1_1 LANGUAGES CXX)

find_package(ZLIB)

add_library(${PROJECT_NAME} SHARED)

target_sources(${PROJECT_NAME}
	PRIVATE
		src/alpha1_1.cpp
)

target_include_directories(${PROJECT_NAME}
	PUBLIC
		${CMAKE_CURRENT_SOURCE_DIR}/include
)

target_link_libraries(${PROJECT_NAME}
	PUBLIC
		headers
		ZLIB::ZLIB
)

install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/Alpha
		TYPE INCLUDE
)