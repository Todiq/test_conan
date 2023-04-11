set(PROJECT_NAME alpha1_1)
project(${PROJECT_NAME} LANGUAGES CXX)

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
		alpha
		ZLIB::ZLIB
)