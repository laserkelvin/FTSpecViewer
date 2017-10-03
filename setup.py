import os

requirements = ["numpy", "scipy", "pandas",
                "matplotlib", "peakutils", "uncertainties",
                "pyqtgraph"]

for package in requirements:
    os.system("pip install " + package)
