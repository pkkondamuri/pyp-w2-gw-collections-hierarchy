import os
from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ["tests/"]

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import sys, pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='rmotr.com | Collections Hierarchy',
    version='0.0.1',
    description="rmotr.com Group Project | Collections Hierarchy",
    author='rmotr.com',
    author_email='questions@rmotr.com',
    license='CC BY-SA 4.0 License',
    packages=['collections_hierarchy'],
    maintainer='rmotr.com',
    tests_require=[
        'pytest==3.0.2',
        'pytest-cov==2.2.1',
        'coverage==4.0.3',
        'six==1.10.0',
    ],
    zip_safe=False,
    cmdclass={'test': PyTest},
)
