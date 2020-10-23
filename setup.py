#!/usr/bin/env python3
import setuptools

setuptools.setup(
    name="kapitan_helm",
    long_description="",
    version="0.0.2",
    description="Kapitan helm bindings as a python wheel",
    packages=setuptools.find_packages(),
    install_requires=['kapitan', 'cffi>=1.0.0'],
    setup_requires=['setuptools-golang', 'cffi>=1.0.0'],
    ext_modules=[setuptools.Extension('helm', ['main.go'])],
    build_golang={'root': 'github.com/chrisglass/kapitan-helm-bindings'},
    cffi_modules=['cffi_build.py:ffi'],
    zip_safe=False,
)
