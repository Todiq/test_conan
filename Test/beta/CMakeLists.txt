set(PROJECT_NAME beta)
cmake_minimum_required(VERSION 3.15)
project(${PROJECT_NAME} LANGUAGES CXX)

find_package(alpha)

set(OUTPUT ${CMAKE_BINARY_DIR}/output)

if (WIN32)
	set(ALPHA_EXE "${OUTPUT}/alpha_exe.exe")
else()
	set(ALPHA_EXE "${OUTPUT}/alpha_exe")
endif()

add_custom_target(call_alpha_exe ALL
	COMMENT "Calling alpha_exe"
	DEPENDS "${ALPHA_EXE}"
	VERBATIM
	COMMAND "${ALPHA_EXE}"
)

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

add_dependencies(${PROJECT_NAME}
	call_alpha_exe
)

install(TARGETS ${PROJECT_NAME})
