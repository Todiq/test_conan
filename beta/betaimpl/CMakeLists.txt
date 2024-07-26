project(betaimpl LANGUAGES CXX)

add_library(${PROJECT_NAME})


target_sources(${PROJECT_NAME}
	PRIVATE
		src/betaimpl.cpp
)

target_link_libraries(${PROJECT_NAME}
	PRIVATE
        Alpha::test
		ZLIB::ZLIB
)

target_include_directories(${PROJECT_NAME}
	PUBLIC
		${CMAKE_CURRENT_SOURCE_DIR}/include
	PRIVATE
		${CMAKE_CURRENT_SOURCE_DIR}/src
)