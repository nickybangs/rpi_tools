build:
	# bump version number
	pipenv run python -m build

release: build
	# make sure server running on rpi
	pipenv run python -m twine upload -r local dist/*

all: release
	rm dist/*
