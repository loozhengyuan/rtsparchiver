install:
	pip install -r requirements.txt
lint:
	pip install flake8 --upgrade
	flake8
test:
	pip install pytest pytest-cov --upgrade
	pytest