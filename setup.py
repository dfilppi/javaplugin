import setuptools
import os

setuptools.setup(
    name='java-test-plugin',
    version='0.0.1',
    author='dfilppi',
    author_email='dfilppi@gmail.com',
    description='example java plugin for cloudify',
    packages=['java_adapter'],
    package_data = {'java_adapter': [ "plugin.jar" ] },
    install_requires = [
      'cloudify-plugins-common'
    ],
    license='LICENSE'
)
