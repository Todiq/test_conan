set(PROJECT_NAME example)
cmake_minimum_required(VERSION 3.15)
project(${PROJECT_NAME} LANGUAGES CXX)

find_package(alpha)

add_executable(${PROJECT_NAME})

target_sources(${PROJECT_NAME}
	PRIVATE
		example.cpp
)

target_link_libraries(${PROJECT_NAME}
	PUBLIC
		Alpha::alpha1_2
)