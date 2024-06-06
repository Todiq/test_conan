from conan import ConanFile
from collections import namedtuple
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.files import copy, collect_libs
import os

required_conan_version = ">=2.0.0"

class Pkg(ConanFile):
	name = "alpha"
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
		self.requires("rapidjson/cci.20230929")

	def configure(self):
		if self.options.get_safe("shared") is True:
			self.options.rm_safe("fPIC")

	def layout(self):
		cmake_layout(self)
		bt = "." if self.settings.get_safe("os") != "Windows" else str(self.settings.build_type)
		self.cpp.build.components["alpha"].libdirs = [os.path.join("BaseTest", bt)]
		self.cpp.build.components["alpha"].bindirs = [os.path.join("BaseTest", bt)]
		self.cpp.source.components["alpha"].includedirs = ["include"]

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
		self.cpp_info.components["basetest"].libs = [f"alpha"]
		self.cpp_info.components["basetest"].set_property("cmake_target_name", f"Alpha::alpha")
		self.cpp_info.components["basetest"].requires = ["rapidjson::rapidjson"]