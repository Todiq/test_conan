import os

from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.files import copy, collect_libs

class Pkg(ConanFile):
	name = "test_alpha"
	version = "1.0"

	settings = "os", "compiler", "build_type", "arch"
	package_type = "application"


	def export_sources(self):
		copy(self, "src/*", src=self.recipe_folder, dst=self.export_sources_folder)
		copy(self, "include/*", src=self.recipe_folder, dst=self.export_sources_folder)
		copy(self, "CMakeLists.txt", src=self.recipe_folder, dst=self.export_sources_folder)

	def requirements(self):
		self.requires("zlib/[>=1.0 <2.0]")

	def layout(self):
		cmake_layout(self)
		bt = "." if self.settings.get_safe("os") != "Windows" else str(self.settings.build_type)
		ext = "" if self.settings.get_safe("os") != "Windows" else ".exe"

		self.cpp.build.bindirs = [bt]
		self.cpp.build.location = os.path.join(self.folders.build, bt, f"alpha{ext}")

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
		ext = "" if self.settings.get_safe("os") != "Windows" else ".exe"

		self.cpp_info.set_property("cmake_target_name", "Alpha::alpha")
		self.cpp_info.requires = ["zlib::zlib"]
		self.cpp_info.exe = "alpha"
		self.cpp_info.location = os.path.join("bin", f"alpha{ext}")