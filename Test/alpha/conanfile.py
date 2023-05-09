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
		"shared": False,
		"fPIC": True,
	}

	_ParsingComponent = namedtuple("_ParsingComponent", ("path", "contains_headers", "header_only"))
	_parsing_components = {
		"myalpha": _ParsingComponent(".", True, True),
		"alpha1_1": _ParsingComponent("alpha1/alpha1_1", True, False),
		"alpha1_2": _ParsingComponent("alpha1/alpha1_2", True, False),
		"alpha2": _ParsingComponent("alpha2", True, False),
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
		bt_folder = f"/{self.settings.build_type}" if self.settings.compiler == "msvc" else ""

		for compname, comp in self._parsing_components.items():
			if comp.header_only is False:
				self.cpp.build.components[compname].libdirs = [f"{comp.path}{bt_folder}"]
				self.cpp.build.components[compname].bindirs = [f"{comp.path}{bt_folder}"]
			else:
				self.cpp.build.components[compname].libdirs = [f""]
				self.cpp.build.components[compname].bindirs = [f""]
			if comp.contains_headers is True:
				self.cpp.source.components[compname].includedirs = [f"{comp.path}/include"]

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
		for compname, comp in self._parsing_components.items():
			if comp.header_only is True:
				self.cpp_info.components[compname].bindirs = []
				self.cpp_info.components[compname].libdirs = []
			else:
				self.cpp_info.components[compname].libs = [f"{compname}"]
