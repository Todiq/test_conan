from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.files import copy, collect_libs
import os

required_conan_version = ">=2.0.0"

class Pkg(ConanFile):
	name = "test_alpha"
	version = "1.0"

	# Binary configuration
	settings = "os", "compiler", "build_type", "arch"
	implements = ["auto_shared_fpic"]
	options = { "shared": [True, False], "fPIC": [True, False] }
	default_options = { "shared": True, "fPIC": False }

	def export_sources(self):
		to_exclude = ["build"]
		copy(self, "*.cpp", src=self.recipe_folder, dst=self.export_sources_folder, excludes=to_exclude)
		copy(self, "*.hpp", src=self.recipe_folder, dst=self.export_sources_folder, excludes=to_exclude)
		copy(self, "*CMakeLists.txt", src=self.recipe_folder, dst=self.export_sources_folder, excludes=to_exclude)

	def requirements(self):
		self.requires("zlib/1.3.1")

	def configure(self):
		if self.options.get_safe("shared") is True:
			self.options.rm_safe("fPIC")
		self.options["zlib/*"].shared=True

	def layout(self):
		cmake_layout(self)
		bt = "." if self.settings.get_safe("os") != "Windows" else str(self.settings.build_type)
		self.cpp.source.components["test"].includedirs = ["include"]
		self.cpp.build.components["test"].libdirs = [bt]
		self.cpp.build.components["test"].bindirs = [bt]

	def generate(self):
		tc = CMakeToolchain(self)
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
		self.cpp_info.components["test"].libs = ["test"]
		self.cpp_info.components["test"].set_property("cmake_target_name", "Alpha::test")