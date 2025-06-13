import os

from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeConfigDeps, cmake_layout
from conan.tools.files import copy, collect_libs

required_conan_version = ">=2.17.0"

class Pkg(ConanFile):
	name = "test_alpha"
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
		self.requires("zlib/1.3.1", transitive_headers=True)

	def configure(self):
		if self.options.get_safe("shared") is True:
			self.options.rm_safe("fPIC")
		self.options["zlib/*"].shared=True

	def layout(self):
		cmake_layout(self)

	def generate(self):
		tc = CMakeToolchain(self)
		tc.generate()
		d = CMakeConfigDeps(self)
		d.generate()

	def build(self):
		cmake = CMake(self)
		cmake.configure()
		cmake.build()

	def package(self):
		cmake = CMake(self)
		cmake.install()

	def package_info(self):
		ext = ".exe" if self.settings.os == "Windows" else ""
		self.cpp_info.set_property("cmake_target_name", "Alpha::alpha")
		self.cpp_info.requires = ["zlib::zlib"]
		self.cpp_info.exe = [f"alpha{ext}"]
		self.cpp_info.location = f"alpha{ext}"