install:
	./setup.py install

docs: graph/*.py
	epydoc -v --no-frames --no-sourcecode --name="python-graph" --url="http://code.google.com/p/python-graph/" --html -o docs graph/*.py

edit: graph/*.py
	gedit graph/*.py &

clean: graph/*.pyc
	rm graph/*.pyc
