from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in quality_control/__init__.py
from quality_control import __version__ as version

setup(
	name="quality_control",
	version=version,
	description="Quality",
	author="Rehan",
	author_email="rehan@preciholesports.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
