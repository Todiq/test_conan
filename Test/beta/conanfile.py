from collections import namedtuple
from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.files import copy, collect_libs

required_conan_version = ">=2.0.0"

class Pkg(ConanFile):
	name = "beta"
	version = "1.0"

	# Binary configuration
	settings = "os", "compiler", "build_type", "arch"

	def requirements(self):
		self.requires("alpha/1.0")

	def configure(self):
		self.options["alpha/*"].shared=True

	def layout(self):
		cmake_layout(self, generator="Ninja")

	def generate(self):
		tc = CMakeToolchain(self)
		tc.generate()
		d = CMakeDeps(self)
		d.generate()

	def build(self):
		cmake = CMake(self)
		cmake.configure()
		cmake.build()
