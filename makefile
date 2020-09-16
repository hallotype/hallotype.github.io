all: build

build: 
	python3 -B build.py

new:
	python3 -B addProject.py $(name)