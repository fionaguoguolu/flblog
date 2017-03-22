.PHONY: bootstrap
bootstrap:
	python setup.py install

.PHONY: serve
serve:
	# python FLBLOG/webserver.py
	# pip install flask
	# python FLBLOG/webserver2.py flaskapp:app
	python FLBLOG/webserver2.py wsgiapp:app

.PHONY: test
test:
	pytest tests/*

.PHONY: clean
clean:
	rm -rf build/ .cache/ dist/ flblog.egg-info/

.PHONY: lint
lint:
	flake8 FLBLOG/ tests/
