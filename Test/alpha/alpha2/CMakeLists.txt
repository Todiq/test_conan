project(alpha2 LANGUAGES CXX)

add_library(${PROJECT_NAME} SHARED)

target_sources(${PROJECT_NAME}
	PRIVATE
		src/alpha2.cpp
)

target_include_directories(${PROJECT_NAME}
	PUBLIC
		${CMAKE_CURRENT_SOURCE_DIR}/include
)

target_link_libraries(${PROJECT_NAME}
	PUBLIC
		alpha1_1
)

install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/Alpha
		TYPE INCLUDE
)