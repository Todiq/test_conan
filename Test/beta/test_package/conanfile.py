import os
from conan import ConanFile


class Pkg(ConanFile):

	settings = "os"

	def requirements(self):
		self.requires(self.tested_reference_str)

	def test(self):
		self.run("beta", env="conanrun")
