from conan import ConanFile
from collections import namedtuple
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.files import copy, collect_libs
import os

required_conan_version = ">=2.0.0"

class Pkg(ConanFile):
	name = "test_beta"
	version = "1.0"

	# Binary configuration
	settings = "os", "compiler", "build_type", "arch"
	options = { "shared": [True, False], "fPIC": [True, False] }
	default_options = { "shared": True, "fPIC": False }

	def export_sources(self):
		copy(self, "*.cpp", src=self.recipe_folder, dst=self.export_sources_folder, excludes=["build"])
		copy(self, "*.hpp", src=self.recipe_folder, dst=self.export_sources_folder, excludes=["build"])
		copy(self, "*CMakeLists.txt", src=self.recipe_folder, dst=self.export_sources_folder, excludes=["build"])

	def requirements(self):
		self.requires("test_alpha/1.0")
		self.requires("cpython/3.9.19")

	def config_options(self):
		if self.settings.get_safe("os") == "Windows":
			self.options.rm_safe("fPIC")

	def configure(self):
		if self.options.get_safe("shared") is True:
			self.options.rm_safe("fPIC")
		self.options["test_alpha/*"].shared=True

	def layout(self):
		cmake_layout(self)
		bt = "." if self.settings.get_safe("os") != "Windows" else str(self.settings.build_type)
		self.cpp.build.components["beta"].libdirs = [bt]
		self.cpp.build.components["beta"].bindirs = [bt]
		self.cpp.build.components["betaimpl"].libdirs = [os.path.join("betaimpl", bt)]
		self.cpp.build.components["betaimpl"].bindirs = [os.path.join("betaimpl", bt)]

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