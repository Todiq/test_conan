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
	options = {
		"shared": [True, False],
		"fPIC": [True, False],
	}
	default_options = {
		"shared": True,
		"fPIC": False,
	}

	def export_sources(self):
		copy(self, "*.c*", src=self.recipe_folder, dst=self.export_sources_folder)
		copy(self, "*.h*", src=self.recipe_folder, dst=self.export_sources_folder)
		copy(self, "*CMakeLists.txt", src=self.recipe_folder, dst=self.export_sources_folder)

	def requirements(self):
		self.requires("alpha/1.0")

	def configure(self):
		self.options["alpha/*"].shared=True

	def layout(self):
		self.folders.source = "."
		self.folders.build = f"build/{self.settings.build_type}"
		self.folders.generators = f"{self.folders.build}/generators"

		self.cpp.source.includedirs = ["."]
		self.cpp.build.libdirs = ["."]

	def generate(self):
		ct = CMakeToolchain(self)
		ct.generate()
		cd = CMakeDeps(self)
		cd.generate()

	def build(self):
		cmake = CMake(self)
		cmake.configure()
		cmake.build()

	def package(self):
		cmake = CMake(self)
		cmake.install()
