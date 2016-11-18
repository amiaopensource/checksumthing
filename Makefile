PYTHON      ?= python
PIP         ?= pip
TOX         ?= tox
current_dir = $(shell pwd)
DOC_BUILD   = $(current_dir)/docs/build

.PHONY: docs tox-test

all:
	@echo "checksumthing"
	@$(PYTHON) setup.py build

test:
	$(PYTHON) setup.py test

install-tox:
	@$(PIP) install -q tox

install-sphinx:
	@echo 'installing Sphinx'
	@$(PIP) install -q sphinx

install: docs
	@echo "installing checksumthing"
	@$(PYTHON) setup.py install

docs: install-sphinx
	@echo 'creating Sphinx documentation'
	@$(PYTHON) setup.py build_sphinx

tox-test: install-tox
	@echo 'running tox tests'
	@$(TOX)

clean:
	@$(PYTHON) setup.py clean

	@if [ -d docs/build ]; then \
	    	echo 'deleting generated documentation'; \
		rm -R docs/build; \
    	fi

	@if [ -d build ]; then \
	    	echo 'deleting build'; \
    		rm -R build; \
    	fi

	@if [ -d dist ]; then \
		echo 'deleting dist'; \
		rm -R dist; \
	fi

	@if [ -d .tox ]; then \
		echo 'deleting tox cache'; \
		rm -R .tox; \
	fi

	@if [ -d .eggs ]; then \
		echo 'deleting .egg cache'; \
		rm -R .eggs; \
	fi

	@if [ -d .cache ]; then \
		rm -R .cache; \
	fi

	@if [ -d checksumthing.egg-info ]; then \
		echo 'Deleting checksumthing.egg-info.'; \
		rm -R checksumthing.egg-info; \
	fi


uninstall:
	@echo 'Uninstalling Checksumthing'
	@$(PIP) uninstall Checksumthing -y
