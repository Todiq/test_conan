project(alpha_exe LANGUAGES CXX)

add_executable(${PROJECT_NAME})

target_sources(${PROJECT_NAME}
	PRIVATE
		src/alpha_exe.cpp
)

target_link_libraries(${PROJECT_NAME}
	PUBLIC
		headers
		alpha2
)