Development environment
Windows 10

IDE Pycharm

python3 version: 3.6

# MAIN PROGRAM
L-Est97 to WGS84 and WGS84 TO L-Est978 coordinates converter

Converting code is located in coordinates.main file.

Simple application for converting L-Est97 to WGS84 coordinates and vice versa.

This application has GUI made in Flask and also by using Tkinter tools.

To run this conversion program in WEB, download flaskProject and run app.py.

It uses installed module for converting coordinates, so before using, you should
make sure, that necessary module is installed.

Use: ```pip install -i https://test.pypi.org/simple/ example-package-dakurb```

To run this conversion program as Tkinter program, just run method
converter_ui() in coordinates.main


# TESTS
Test code is located in tests.test_convertings file.

Tests are written in pytest and for running tests, pytest is needed.

To install pytest run:
```pip install pytest```

To execute test suite:
```python -m pytest tests/```

