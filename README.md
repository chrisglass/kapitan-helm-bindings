kapitan-helm-bindings
======================


This project is  an attempt at packaging the kapitan helm bindings separately
from the kapitan project, in order to be able to "pip install" the helm bindings
instead of having to build them inside the kapitan tree.

This project is UNFINISHED and not currently useable (see below).

Current approach and findings
------------------------------

The approach taken by this project is to build the golang extension using
`setuptools-golang`.

This succesfully builds a golang binary in shared library mode, that we then
build a cffi wrapper for.

The compilation method used is "out-of-line" and "ABI mode" as described in https://cffi.readthedocs.io/en/latest/cdef.html


Building and publishing
-----------------------

The following steps are required to build and publish the wheel(s) to pypi:

- In a virtualenv with the build dependencies available ('setuptools-golang', 'cffi>=1.0.0'), run 
`setuptools-golang-build-manylinux-wheels`
- Once the build process is over you can upload the resulting wheels (located in dist/):
`twine upload --repository testpypi dist/**`

Future work
-----------

There's a few things to do for this to be successful:

- ensure the resulting package is useable stand alone (eg. pip install the
  package, checkout a helm chart, and ensure it compiles from the python REPL)
- once the package is ready, some work with upstream needs to happen:

    - publish the package with a rational namespace (kapitan-helm-binding might
      not be the most desirable)
    - open a PR against kapitan to use the published helm binding package
      instead of the in-tree compilation. The user experience for kapitan is
      significantly better this way: "pip install kapitan" gets the main
      kapitan, then "pip install kapitan-helm-binding" grabs the wheel
      containing the bindings binary/cffi)
    - finally change commodore to use the published kapitan-helm-binding package
      as well.
