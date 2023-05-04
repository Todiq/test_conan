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

		self.cpp.source.components["alpha_alpha1_1"].includedirs = ["alpha1/alpha1_1/include"]
		self.cpp.source.components["alpha_alpha1_2"].includedirs = ["alpha1/alpha1_2/include"]
		self.cpp.source.components["alpha_alpha2"].includedirs = ["alpha2/include"]

		bt_folder = f"/{self.settings.build_type}" if self.settings.compiler == "msvc" else ""
		self.cpp.build.components["alpha_alpha1_1"].libdirs = [f"alpha1/alpha1_1{bt_folder}"]
		self.cpp.build.components["alpha_alpha1_2"].libdirs = [f"alpha1/alpha1_2{bt_folder}"]
		self.cpp.build.components["alpha_alpha2"].libdirs = [f"alpha2{bt_folder}"]
		
		self.cpp.build.components["alpha_alpha1_1"].bindirs = [f"alpha1/alpha1_1{bt_folder}"]
		self.cpp.build.components["alpha_alpha1_2"].bindirs = [f"alpha1/alpha1_2{bt_folder}"]
		self.cpp.build.components["alpha_alpha2"].bindirs = [f"alpha2{bt_folder}"]
	
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
		self.cpp_info.components["alpha_alpha1_1"].libs = ["alpha1_1"]
		self.cpp_info.components["alpha_alpha1_2"].libs = ["alpha1_2"]
		self.cpp_info.components["alpha_alpha2"].libs = ["alpha2"]
