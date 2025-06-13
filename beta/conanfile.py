import os

from conan import ConanFile
from collections import namedtuple
from conan.tools.cmake import CMake, CMakeToolchain, CMakeConfigDeps, cmake_layout
from conan.tools.files import copy, collect_libs

required_conan_version = ">=2.17.0"

class Pkg(ConanFile):
	name = "test_beta"
	version = "1.0"

	# Binary configuration
	settings = "os", "compiler", "build_type", "arch"
	implements = ["auto_shared_fpic"]
	options = { "shared": [True, False], "fPIC": [True, False] }
	default_options = { "shared": True, "fPIC": False }

	def export_sources(self):
		copy(self, "src/*", src=self.recipe_folder, dst=self.export_sources_folder)
		copy(self, "include/*", src=self.recipe_folder, dst=self.export_sources_folder)
		copy(self, "CMakeLists.txt", src=self.recipe_folder, dst=self.export_sources_folder)

	def requirements(self):
		self.requires("test_alpha/1.0")

	def config_options(self):
		if self.settings.get_safe("os") == "Windows":
			self.options.rm_safe("fPIC")

	def configure(self):
		if self.options.get_safe("shared") is True:
			self.options.rm_safe("fPIC")

	def layout(self):
		cmake_layout(self)

	def generate(self):
		ct = CMakeToolchain(self)
		ct.generate()
		cd = CMakeConfigDeps(self)
		cd.generate()

	def build(self):
		cmake = CMake(self)
		cmake.configure()
		cmake.build()

	def package(self):
		cmake = CMake(self)
		cmake.install()