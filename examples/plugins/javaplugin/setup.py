import setuptools
import os

files = None
for _,_,files in os.walk('java_adapter/jars'):
  files = files

setuptools.setup(
    name='java-test-plugin',
    version='0.0.1',
    author='dfilppi',
    author_email='dfilppi@gmail.com',
    description='example java plugin for cloudify',
    packages=['java_adapter'],
    package_data = {'java_adapter': [ 'jars/'+ f for f in files ] },
    install_requires = [
      'cloudify-plugins-common'
    ],
    license='LICENSE'
)
