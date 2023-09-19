set(PROJECT_NAME beta)
cmake_minimum_required(VERSION 3.15)
project(${PROJECT_NAME} LANGUAGES CXX)

find_package(alpha)

add_library(${PROJECT_NAME} SHARED)

target_sources(${PROJECT_NAME}
	PRIVATE
		src/beta.cpp
)

target_link_libraries(${PROJECT_NAME}
	PUBLIC
		Alpha::headers
		Alpha::alpha2
)

install(TARGETS ${PROJECT_NAME})
