#!/usr/bin/env python

import sys
import setuptools

from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

version = '1.0.10'
setuptools.setup(name='centos_package_cron',
      version=version,
      description='CentOS Package Update Utilities',
      author='Brady Wied',
      author_email='support@bswtechconsulting.com',
      url='https://github.com/wied03/centos-package-cron',
      download_url='https://github.com/wied03/centos-package-cron/archive/releases/%s.tar.gz' % (version),
      license='BSD 2-Clause',
      packages=setuptools.find_packages(),
      setup_requires="pytest",
      install_requires=['sqlalchemy<1.2', 'wheel==0.16.0', 'requests[security]==2.19.1'],
      tests_require="mock==2.0.0",
      cmdclass = {'test': PyTest},
	  entry_points = {
	        'console_scripts': ['centos-package-cron=centos_package_cron.command_line:main'],
	  }
     )
