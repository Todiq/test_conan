import os

from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.files import copy, collect_libs

required_conan_version = ">=2.20.1"

class Pkg(ConanFile):
	name = "test_alpha"
	version = "1.0"

	settings = "os", "compiler", "build_type", "arch"
	implements = ["auto_shared_fpic"]
	package_type = "application"


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
		bt = "." if self.settings.get_safe("os") != "Windows" else str(self.settings.build_type)
		ext = "" if self.settings.get_safe("os") != "Windows" else ".exe"
		self.cpp.build.location = os.path.join(self.folders.build, bt, f"alpha{ext}")
		self.cpp.package.location = os.path.join(self.folders.package, "bin", f"alpha{ext}")
		self.layouts.build.buildenv_info.define_path("MY_TXT", "test.txt")
		self.layouts.build.runenv_info.define_path("MY_TXT", "test.txt")

		self.layouts.package.buildenv_info.define_path("MY_TXT", os.path.join("share", "test.txt"))
		self.layouts.package.runenv_info.define_path("MY_TXT", os.path.join("share", "test.txt"))

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
		self.cpp_info.set_property("cmake_target_name", "Alpha::alpha")
		self.cpp_info.requires = ["zlib::zlib"]
		self.cpp_info.exe = "alpha"