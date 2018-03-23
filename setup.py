# Copyright Notice:
# Copyright 2017 Distributed Management Task Force, Inc. All rights reserved.
# License: BSD 3-Clause License. For full text see link: https://github.com/DMTF/libredfish/blob/master/LICENSE.md
from distutils.core import setup, Extension

module1 = Extension('libredfish',
                    define_macros = [('NO_CZMQ', 1)],
                    include_dirs = ['include'],
                    libraries = ['jansson', 'curl'],
                    sources = ['src/main.c', 'src/payload.c', 'src/redpath.c', 'src/service.c', 'bindings/python/pyredfish.c'])

setup (name = 'libRedfish',
       version = '1.0',
       ext_modules = [module1])
