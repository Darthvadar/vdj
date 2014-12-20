# Copyright 2014 Uri Laserson
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from glob import glob

from setuptools import setup, find_packages
from numpy.distutils.core import Extension
from numpy.distutils.misc_util import get_numpy_include_dirs


alignment_core_ext = Extension(
    'vdj.alignmentcore',
    ['vdj/alignmentcore.c'],
    include_dirs=get_numpy_include_dirs())

clustering_core_ext = Extension(
    'vdj.clusteringcore',
    ['vdj/clusteringcore.c'],
    include_dirs=get_numpy_include_dirs())

def readme():
    with open('README.md', 'r') as ip:
        return ip.read()

setup(
    name='vdj',
    version='0.2.0-dev',
    description='Python package for immune receptor sequence data',
    long_description=readme(),
    author='Uri Laserson',
    author_email='uri.laserson@gmail.com',
    url='https://github.com/churchlab/vdj',
    packages=find_packages(),
    package_data={'vdj': ['data/*.fasta']},
    ext_modules=[alignment_core_ext, clustering_core_ext],
    scripts=glob('bin/*.py'),
    install_requires=['numpy', 'scipy', 'biopython'],
    keywords=('vdj immune repertoire antibody tcr sequencing dna '
              'alignment clustering'),
    license='Apache License, Version 2.0',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ],
    zip_safe=False
)
