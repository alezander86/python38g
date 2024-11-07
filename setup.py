from version import __version__
from setuptools import find_packages, setup
from setuptools import Command


class VersionCommand(Command):
    description = "Printing version of the package"
    
    user_options = []

    def initialize_options(self):
        """Override default one if needed"""   
    def finalize_options(self):
        """Override default one if needed"""
    def run(self):
        print(__version__)

setup(
    name='hello_world',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,

    cmdclass={'version': VersionCommand},

    setup_requires=['pytest-runner'],
    tests_require=["pytest","requests"],

    install_requires=[
        "Click==8.1.7",
        "Flask==3.0.3",
        "Jinja2==3.1.4",
        "MarkupSafe==2.1.5",
        "Werkzeug==3.0.6",
        "markdown==3.7",
        ],
)
