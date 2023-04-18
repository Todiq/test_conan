set(PROJECT_NAME beta)
cmake_minimum_required(VERSION 3.15)
project(${PROJECT_NAME} LANGUAGES CXX)

find_package(alpha)

add_executable(${PROJECT_NAME})

target_sources(${PROJECT_NAME}
	PRIVATE
		beta.cpp
)

target_include_directories(${PROJECT_NAME}
	PUBLIC
		${CMAKE_CURRENT_SOURCE_DIR}/include
)

target_link_libraries(${PROJECT_NAME}
	PUBLIC
		alpha::alpha
)

add_custom_target(test ALL
	COMMENT "Running beta"
	VERBATIM
	COMMAND $<TARGET_FILE:${PROJECT_NAME}>
)

add_dependencies(test
	beta
)