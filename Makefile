.PHONY: bootstrap
bootstrap:
	python setup.py install

.PHONY: test
test:
	pytest tests/*

.PHONY: clean
clean:
	rm -rf build/ .cache/ dist/ flblog.egg-info/
