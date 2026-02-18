import os

from conan import ConanFile
from collections import namedtuple
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.files import copy, collect_libs

class Pkg(ConanFile):
	name = "test_gamma"
	version = "1.0"
	settings = "os", "compiler", "build_type", "arch"
	package_type = "application"

	def export_sources(self):
		# copy(self, "src/*", src=self.recipe_folder, dst=self.export_sources_folder)
		# copy(self, "include/*", src=self.recipe_folder, dst=self.export_sources_folder)
		copy(self, "CMakeLists.txt", src=self.recipe_folder, dst=self.export_sources_folder)

	def requirements(self):
		self.requires("test_beta/[>=1.0 <2.0]")

	def layout(self):
		cmake_layout(self)

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