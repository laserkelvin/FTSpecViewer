import os

requirements = ["numpy", "scipy", "pandas",
                "matplotlib", "peakutils", "uncertainties"]

for package in requirements:
    os.system("pip install " + package)

