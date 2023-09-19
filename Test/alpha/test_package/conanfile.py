import os
from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout


class Pkg(ConanFile):

	# Binary configuration
	settings = "os", "compiler", "build_type", "arch"
	generators = "CMakeDeps", "CMakeToolchain"

	def build_requirements(self):
		self.tool_requires(self.tested_reference_str)

	def requirements(self):
		self.requires(self.tested_reference_str)

	# def layout(self):
	# 	cmake_layout(self)

	# def build(self):
	# 	cmake = CMake(self)
	# 	cmake.configure()
	# 	cmake.build()

	# def test(self):
	# 	extension = ".exe" if self.settings_build.os == "Windows" else ""
	# 	self.run("alpha_exe{} mypath".format(extension))
		# cmd = os.path.join(self.cpp.build.bindir, "example")
		# self.run(cmd, env="conanrun")