import os

from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.files import copy, collect_libs

class Pkg(ConanFile):
	name = "test_alpha"
	version = "1.0"

	settings = "os", "compiler", "build_type", "arch"
	package_type = "shared-library"
	implements = ["auto_shared_fpic"]

	# Binary configuration
	options = {
		"shared": [True, False],
		"fPIC": [True, False]
	}
	default_options = {
		"shared": False,
		"fPIC": True
	}


	def export_sources(self):
		copy(self, "src/*", src=self.recipe_folder, dst=self.export_sources_folder)
		copy(self, "include/*", src=self.recipe_folder, dst=self.export_sources_folder)
		copy(self, "CMakeLists.txt", src=self.recipe_folder, dst=self.export_sources_folder)

	def layout(self):
		cmake_layout(self)

	def generate(self):
		tc = CMakeToolchain(self)
		tc.cache_variables["PROJECT_VERSION"] = self.version
		tc.generate()
		d = CMakeDeps(self)
		d.generate()

	def build(self):
		cmake = CMake(self)
		cmake.configure()
		cmake.build()

	def package(self):
		cmake = CMake(self)
		cmake.install()

	def package_info(self):
		self.cpp_info.libs = ["alpha"]
		self.cpp_info.set_property("cmake_target_name", "Alpha::alpha")