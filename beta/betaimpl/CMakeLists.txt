project(betaimpl LANGUAGES CXX)

add_library(${PROJECT_NAME})

target_sources(${PROJECT_NAME}
	PRIVATE
		src/betaimpl.cpp
)

target_link_libraries(${PROJECT_NAME}
	PRIVATE
        Alpha::test
		Python::Python
)

target_include_directories(${PROJECT_NAME}
	PUBLIC
		${CMAKE_CURRENT_SOURCE_DIR}/include
	PRIVATE
		${CMAKE_CURRENT_SOURCE_DIR}/src
)

install(TARGETS ${PROJECT_NAME}
	RUNTIME_DEPENDENCY_SET my_app_deps
	RUNTIME
		DESTINATION "${CMAKE_BINARY_DIR}"
	LIBRARY
		DESTINATION "${CMAKE_LIBRARY_DIR}"
	ARCHIVE
		DESTINATION "${CMAKE_ARCHIVE_DIR}"
)