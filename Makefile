build:
	setuptools-golang-build-manylinux-wheels

clean:
	rm -f kapitan_helm/*.so
	rm -f kapitan_helm/*.h
	rm -rf .eggs/
	rm -rf build/
	rm -rf *.egg-info/
	rm -rf dist/
