set(PROJECT_NAME beta)
cmake_minimum_required(VERSION 3.15)
project(${PROJECT_NAME} LANGUAGES CXX)

find_package(alpha)

add_executable(${PROJECT_NAME})

target_sources(${PROJECT_NAME}
	PRIVATE
		beta.cpp
)

target_link_libraries(${PROJECT_NAME}
	PUBLIC
		alpha::alpha1_2
)

install(TARGETS ${PROJECT_NAME})
