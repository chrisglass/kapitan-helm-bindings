#!/usr/bin/env bash

echo "This is provided for reference and will be deleted in the future"
echo "If you are trying to build this as a python module, run this instead:"
echo "   setuptools-golang-build-manylinux-wheels "
exit 0

cd $(dirname "$0")
pwd

so_name="kapitan_helm/libtemplate.so"

# Compile the binding if a Go runtime exists
if [[ -z $(which go) ]]; then
    echo "[WARN] go is not available on this system -- skipping Helm binding build!"
else
    go build -buildmode=c-shared -o $so_name template.go
fi

# Validate that the compiled binding exists
if [[ -e $so_name ]]; then
    echo "[INFO] $so_name built successfully or already exists"
else
    echo "[ERROR] $so_name does not exist!"
    exit 1
fi

# Compile the Python ffi binding if Python is available
if [[ -z $(which python3) ]]; then
    echo "[WARN] python3 is not available on this system -- skipping cffi build!"
else
    echo "[INFO] Building the Python binding using cffi"
    python3 cffi_build.py
fi

exit 0
