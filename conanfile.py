from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.files import copy, collect_libs

required_conan_version = ">=2.0.0"

class Pkg(ConanFile):
	name = "example"
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
		copy(self, "*.cpp", src=self.recipe_folder, dst=self.export_sources_folder, excludes=["build"])
		copy(self, "*CMakeLists.txt", src=self.recipe_folder, dst=self.export_sources_folder, excludes=["build"])

	def config_options(self):
		if self.settings.os == "Windows":
			del self.options.fPIC

	def configure(self):
		if self.options.shared:
			self.options.rm_safe("fPIC")

	def layout(self):
		cmake_layout(self, generator="Ninja")

	def generate(self):
		ct = CMakeToolchain(self, generator="Ninja")
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
		self.cpp_info.libdirs = ["lib", "lib64"]
		self.cpp_info.libs = collect_libs(self)
