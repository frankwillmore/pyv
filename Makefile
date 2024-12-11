v: src/v.c
	$(CC) -c -fPIC src/v.c -o src/v.o
	$(CC) -shared src/v.o -o src/libv.so

pypi: v v.py setup.py
	grayskull pypi v
	sed -ie "s/PLEASE_ADD_LICENSE_FILE/LICENSE/g" v/meta.yaml

build: 
	conda-build v

install:
	conda install --use-local v

PHONY: pypi
