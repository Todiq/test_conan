from collections import namedtuple
from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.files import copy
import os

required_conan_version = ">=2.0.0"

class Pkg(ConanFile):
	name = "alpha"
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
		copy(self, "*.cpp", src=self.recipe_folder, dst=self.export_sources_folder)
		copy(self, "*.hpp", src=self.recipe_folder, dst=self.export_sources_folder)
		copy(self, "*CMakeLists.txt", src=self.recipe_folder, dst=self.export_sources_folder)

	def requirements(self):
		self.requires("zlib/1.2.13")

	def config_options(self):
		if self.settings.os == "Windows":
			self.options.rm_safe("fPIC")

	def configure(self):
		if self.options.shared:
			self.options.rm_safe("fPIC")
		self.options["zlib/*"].shared=True

	def layout(self):
		cmake_layout(self)
		bt = "." if self.settings.os != "Windows" else str(self.settings.build_type)

		self.cpp.source.components["headers"].includedirs = ["include"]
		self.cpp.source.components["alpha1"].includedirs = ["alpha1/include"]
		self.cpp.build.components["alpha1"].libdirs = [os.path.join("alpha1", bt)]
		self.cpp.source.components["alpha2"].includedirs = ["alpha2/include"]
		self.cpp.build.components["alpha2"].libdirs = [os.path.join("alpha2", bt)]
		self.cpp.build.components["alpha_exe"].includedirs = []
		self.cpp.build.components["alpha_exe"].libdirs = []
		self.cpp.build.components["alpha_exe"].bindirs = [os.path.join("alpha_exe", bt)]
		self.cpp.build.components["alpha_exe"].resdirs = ["alpha_exe"]
		self.cpp.package.components["alpha_exe"].resdirs = ["share"]

	def generate(self):
		tc = CMakeToolchain(self)
		tc.generate()
		d = CMakeDeps(self)
		d.generate()

	def build(self):
		cmake = CMake(self)
		cmake.configure()
		cmake.build()
		if self.conf.get("tools.build:skip_test") is False:
			resdirs = self.cpp_info.components["alpha_exe"].resdirs
			# Manipulation with hello.txt
			print(f"resdirs : {resdirs}")

	def package(self):
		cmake = CMake(self)
		cmake.install()

	def package_info(self):
		self.cpp_info.resdirs = ["share"]
		self.cpp_info.components["headers"].set_property("cmake_target_name", "Alpha::headers")
		self.cpp_info.components["alpha1"].libs = ["alpha1"]
		self.cpp_info.components["alpha1"].set_property("cmake_target_name", "Alpha::alpha1")
		self.cpp_info.components["alpha2"].libs = ["alpha2"]
		self.cpp_info.components["alpha2"].set_property("cmake_target_name", "Alpha::alpha2")
