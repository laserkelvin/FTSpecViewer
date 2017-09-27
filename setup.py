from setuptools import setup
from setuptools.command.install import install
import os
from distutils.spawn import find_executable
import stat
import sys

class PostInstallCommand(install):

    def run(self):
        format_dict = {"python_path": sys.executable}
        if os.path.isdir(os.path.expanduser("~") + "/bin") is False:
            os.mkdir(os.path.expanduser("~") + "/bin")
        install.run(self)

setup(
    name="FTSpecViewer",
    version="0.1.0",
    description="An analysis tool for FTMW spectra written in PyQt5.",
    author="Kelvin Lee",
    packages=["ftspecviewer"],
    include_package_data=True,
    author_email="kin_long_kelvin.lee@cfa.harvard.edu",
    install_requires=[
            "numpy",
            "pandas",
            "scipy",
            "matplotlib",
            "peakutils",
            "uncertainties"
    ],
    cmdclass={
        "develop": PostInstallCommand,
        "install": PostInstallCommand
    }
)
