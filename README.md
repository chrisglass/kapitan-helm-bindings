kapitan-helm-bindings
======================


This project is  an attempt at packaging the kapitan helm bindings separately
from the kapitan project, in order to be able to "pip install" the helm bindings
instead of having to build them inside the kapitan tree.

Usage
-----

As a user of kapitan, the desired workflow to use the helm input type is:

``` sh
pip install kapitan
pip install kapitan_helm
```

Current approach and findings
------------------------------

The approach taken by this project is to build the golang extension using
`setuptools-golang`.

This successfully builds a golang binary in shared library mode, that we then
build a cffi wrapper for.

The compilation method used is "out-of-line" and "ABI mode" as described in https://cffi.readthedocs.io/en/latest/cdef.html

This blog post was very helpful to understand the various CFFI extensions used
https://blog.schuetze.link/2018/07/21/a-dive-into-packaging-native-python-extensions.html

Building and publishing
-----------------------

The following steps are required to build and publish the wheel(s) to pypi:

- In a virtualenv with the build dependencies available ('setuptools-golang', 'cffi>=1.0.0'), run 
`setuptools-golang-build-manylinux-wheels`
- Once the build process is over you can upload the resulting wheels (located in dist/):
`twine upload --repository testpypi dist/**`

More information can be found here: https://packaging.python.org/tutorials/packaging-projects/
