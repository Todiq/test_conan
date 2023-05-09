project(alpha1_2 LANGUAGES CXX)

add_library(${PROJECT_NAME} SHARED)

target_sources(${PROJECT_NAME}
	PRIVATE
		src/alpha1_2.cpp
)

target_include_directories(${PROJECT_NAME}
	PUBLIC
		${CMAKE_CURRENT_SOURCE_DIR}/include
)

set_target_properties(${PROJECT_NAME} PROPERTIES PUBLIC_HEADER "${CMAKE_CURRENT_SOURCE_DIR}/include/alpha/alpha1_2/alpha1_2.hpp")

target_link_libraries(${PROJECT_NAME}
	PUBLIC
		myalpha
		alpha1_1
)

install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/Alpha
		TYPE INCLUDE
)