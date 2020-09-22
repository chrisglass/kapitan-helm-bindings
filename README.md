kapitan-helm-bindings
======================


This project is  an attempt at packaging the kapitan helm bindings separately
from the kapitan project, in order to be able to "pip install" the helm bindings
instead of having to build them inside the kapitan tree.

This project is UNFINISHED and not currently useable (see below).

Current approach and findings
------------------------------

The first approach taken by this project is to attempt to build the golang
extension using setuptools-golang.

This seems to successfully build the golang code into a shared .so object that
we can inspect and call from python - however the kapitan helm bindings
currently use CFFI instead of ctypes, so the CFFI part is not currenlty "hooked
in" to the build.

During this process a bug was found in setuptools-golang: setuptools-golang
first issues a "go get -d" in GOPATH mode, that checks out all dependencies in a
/tmp subdirectory, marking the whole hierarchy read-only (including
directories). Once the build is done, the code tries to delete the temporary
tree, but that fails since all of the path is marked read-only. A bit of logic
meant for windows tries to set the file as "write-only" in order to be able to
delete it, but that fails on linux since the directory is marked read-only as
well.

Future work
-----------

There's a few things to do for this to be successful:

- find or write code to run the CFFI precompilation properly on the built golang
  .so (CFFI precompiles a "wrapper" class).
- fix the found bug in setuptools-golang
- extend setuptools-golang to run the cffi compilation (if needed/detected)
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
