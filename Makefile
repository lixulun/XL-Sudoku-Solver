SETUP = python3 setup.py

test:
	$(SETUP) test

build:
	$(SETUP) build
	$(SETUP) sdist bdist_wheel bdist_egg

develop:
	$(SETUP) develop

undevelop:
	$(SETUP) develop --uninstall

install:
	$(SETUP) install

clean:
	$(SETUP) clean --all