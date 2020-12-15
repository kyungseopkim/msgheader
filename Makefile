LIB_DIR = lib

.PHONY: clean

msgheader.cpython-39-darwin.so: setup.py msgheader.pyx $(LIB_DIR)/libmsgheader.a
	python3 setup.py build_ext --inplace 

$(LIB_DIR)/libmsgheader.a:
	make -C $(LIB_DIR) libmsgheader.a

dist: msgheader.cpython-39-darwin.so
	python setup.py bdist_wheel

clean:
	rm -rf *.so build dist msgheader.c *.egg-info __pycache__ MANIFEST
	make -C $(LIB_DIR) clean 
