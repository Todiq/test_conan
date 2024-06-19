from conan import ConanFile
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
		self.requires("cpython/3.9.19")
		self.requires("boost/1.81.0")

	def configure(self):
		if self.options.get_safe("shared") is True:
			self.options.rm_safe("fPIC")
		self.options["boost/*"].bzip2=False
		self.options["boost/*"].shared=True
		self.options["boost/*"].without_python=False
		self.options["boost/*"].without_stacktrace=True
		self.options["boost/*"].zlib=False
		self.options["cpython/*"].shared=True
		self.options["cpython/*"].optimizations=False
		self.options["cpython/*"].lto=False
		self.options["cpython/*"].docstrings=False
		self.options["cpython/*"].pymalloc=False
		self.options["cpython/*"].with_bz2=False
		self.options["cpython/*"].with_gdbm=False
		self.options["cpython/*"].with_nis=False
		self.options["cpython/*"].with_sqlite3=False
		self.options["cpython/*"].with_tkinter=False
		self.options["cpython/*"].with_curses=False
		self.options["cpython/*"].with_lzma=False

	def layout(self):
		cmake_layout(self)
		bt = "." if self.settings.get_safe("os") != "Windows" else str(self.settings.build_type)
		self.cpp.source.components["hello"].includedirs = ["include"]
		self.cpp.build.components["hello"].libdirs = [bt]
		self.cpp.build.components["hello"].bindirs = [bt]

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
		self.cpp_info.components["hello"].libs = ["hello"]
		self.cpp_info.components["hello"].set_property("cmake_target_name", "Alpha::hello")
		self.cpp_info.components["hello"].requires = [
			"boost::python",
			"cpython::cpython"
		]