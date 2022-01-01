import setuptools
import sr_u2s

def get_long_description():
    with open("README.md", "r") as readme_file:
        readme = readme_file.read()
        return readme[readme.find("# snowrunner-uwp2steam"):]

if __name__ == '__main__':
	setuptools.setup(
		name=sr_u2s.__name__,
		version=sr_u2s.__version__,
		author="NeryK",
		author_email="96932938+NeryK@users.noreply.github.com",
		description=sr_u2s.__doc__,
		long_description=get_long_description(),
		long_description_content_type="text/markdown",
		url="https://github.com/NeryK/snowrunner-uwp2steam",
		python_requires=">=3",
		packages=[sr_u2s.__package__],
        license="License :: OSI Approved :: BSD License",
        classifiers=[
            "Development Status :: 4 - Beta",
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: BSD License",
            "Operating System :: OS Independent",
            "Topic :: Games/Entertainment"
        ]
    )
