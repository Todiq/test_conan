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
		self.requires("boost/1.85.0", transitive_headers=True)

	def configure(self):
		if self.options.get_safe("shared") is True:
			self.options.rm_safe("fPIC")
		self.options["boost/*"].bzip2=False
		self.options["boost/*"].shared=True
		self.options["boost/*"].zlib=False
		self.options["boost/*"].without_atomic=False
		self.options["boost/*"].without_charconv=True
		self.options["boost/*"].without_chrono=False
		self.options["boost/*"].without_cobalt=True
		self.options["boost/*"].without_container=False
		self.options["boost/*"].without_context=True
		self.options["boost/*"].without_contract=True
		self.options["boost/*"].without_coroutine=True
		self.options["boost/*"].without_date_time=False
		self.options["boost/*"].without_exception=False
		self.options["boost/*"].without_fiber=True
		self.options["boost/*"].without_filesystem=False
		self.options["boost/*"].without_graph=True
		self.options["boost/*"].without_graph_parallel=True
		self.options["boost/*"].without_iostreams=False
		self.options["boost/*"].without_json=True
		self.options["boost/*"].without_locale=False
		self.options["boost/*"].without_log=False
		self.options["boost/*"].without_math=True
		self.options["boost/*"].without_mpi=True
		self.options["boost/*"].without_nowide=True
		self.options["boost/*"].without_program_options=False
		self.options["boost/*"].without_python=False
		self.options["boost/*"].without_random=False
		self.options["boost/*"].without_regex=False
		self.options["boost/*"].without_serialization=True
		self.options["boost/*"].without_stacktrace=True
		self.options["boost/*"].without_system=False
		self.options["boost/*"].without_test=True
		self.options["boost/*"].without_thread=False
		self.options["boost/*"].without_timer=True
		self.options["boost/*"].without_type_erasure=True
		self.options["boost/*"].without_url=True
		self.options["boost/*"].without_wave=True

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
		self.cpp_info.requires = ["boost::thread"]
		self.cpp_info.exe = [f"alpha{ext}"]
		self.cpp_info.location = f"alpha{ext}"