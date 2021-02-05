.PHONY: clean virtualenv test docker dist dist-upload

clean:
	find . -name '*.py[co]' -delete
	rm -rf env/*
	rm -rf venv/*

virtualenv:
	virtualenv --prompt '|> pwmanager <| ' env
	env/bin/pip install -r requirements-dev.txt
	env/bin/python setup.py develop
	chmod +x env/bin/activate
	@echo
	@echo "VirtualENV Setup Complete. Now run: source env/bin/activate (or the must appropriate version to your distribution)"
	@echo

test:
	python -m pytest \
		-v \
		--cov=pwmanager \
		--cov-report=term \
		--cov-report=html:coverage-report \
		tests/

docker: clean
	podman build -t pwmanager:latest .
	@echo
	@echo "Let's test the docker image"
	@echo
	podman run -it pwmanager --help

dist: clean
	rm -rf dist/*
	python setup.py sdist
	python setup.py bdist_wheel

dist-upload:
	twine upload dist/*
