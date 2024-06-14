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
		self.requires("boost/1.81.0")
		self.requires("icu/72.1")
		self.requires("libxml2/2.11.6")
		self.requires("libxslt/1.1.34")
		self.requires("pugixml/1.13")
		self.requires("rapidjson/cci.20230929", transitive_headers=True)
		self.requires("xerces-c/3.2.4")

	def configure(self):
		if self.options.get_safe("shared") is True:
			self.options.rm_safe("fPIC")
		if self.settings.get_safe("os") != "Windows":
			self.options["icu/*"].data_packaging="library"
		self.options["boost/*"].bzip2=False
		self.options["boost/*"].shared=True
		self.options["boost/*"].without_python=False
		self.options["boost/*"].without_stacktrace=True
		self.options["boost/*"].zlib=False
		self.options["icu/*"].shared=True
		self.options["libxml2/*"].shared=True
		self.options["libxml2/*"].zlib=False
		self.options["libxslt/*"].shared=True
		self.options["pugixml/*"].header_only=True
		self.options["xerces-c/*"].shared=True
		self.options["xerces-c/*"].char_type="char16_t"

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
			"boost::headers", "boost::filesystem", "boost::iostreams", "boost::locale", "boost::log", "boost::regex",
			"icu::icu-data", "icu::icu-i18n",
			"libxml2::libxml2",
			"libxslt::libxslt",
			"pugixml::pugixml",
			"rapidjson::rapidjson",
			"xerces-c::xerces-c"
		]