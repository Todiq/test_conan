from collections import namedtuple
from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.files import copy

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

	_AlphaComponent = namedtuple("_AlphaComponent", ("dependencies", "external_dependencies", "is_lib"))
	_alpha_component_tree = {
		"alpha": _AlphaComponent([], [], False),
		"alpha1_1": _AlphaComponent(["alpha"], ["zlib::zlib"], True),
		"alpha1_2": _AlphaComponent(["alpha1_1"], [], True),
		"alpha2": _AlphaComponent([], [], True)
	}

	def export_sources(self):
		copy(self, "*.c*", src=self.recipe_folder, dst=self.export_sources_folder)
		copy(self, "*.h*", src=self.recipe_folder, dst=self.export_sources_folder)
		copy(self, "*CMakeLists.txt", src=self.recipe_folder, dst=self.export_sources_folder)

	def requirements(self):
		self.requires("zlib/1.2.13")

	def configure(self):
		if self.options.shared:
			self.options.rm_safe("fPIC")
		self.options["zlib/*"].shared=True

	def layout(self):
		self.folders.source = "."
		self.folders.build = f"build/{self.settings.build_type}"
		self.folders.generators = f"{self.folders.build}/generators"

		for compname, comp in self._alpha_component_tree.items():
			conan_component = f"{self.name}_{compname.lower()}"
			self.cpp.source.components[conan_component].includedirs = ["."]
			if comp.is_lib:
				self.cpp.build.components[conan_component].libdirs = ["."]

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

	def package_info(self):
		for compname, comp in self._alpha_component_tree.items():
			requires = comp.dependencies + comp.external_dependencies
			if comp.is_lib:
				self.cpp_info.components[compname].libs = [f"{compname}"]
			self.cpp_info.components[compname].requires = requires
