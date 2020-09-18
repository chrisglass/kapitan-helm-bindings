#!/usr/bin/env python3
import setuptools

setuptools.setup(
    name="kapitan_helm",
    long_description="",
    version="0.0.0",
    description="Kapitan helm bindings as a python wheel",
    packages=setuptools.find_packages(),
    install_requires=['kapitan'],
    setup_requires=['setuptools-golang'],
    ext_modules=[setuptools.Extension('template', ['template.go'])],
    build_golang={'root': 'github.com/chrisglass/kapitan-helm-bindings'},
)
