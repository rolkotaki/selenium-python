# Selenium with Python
Basic Selenium framework with pytest and unittest to write automated tests for webpages easily and quickly.

## Description

This is a basic framework with Selenium that could be used to write automated tests for webpages.
<br>
The framework provides a quite simple way of performing browser operations such as getting an element, clicking, setting input values and asserting if an element is enabled or not. Using the element names defined in the model classes, we can easily write the test codes.
<br>
The test cases are written using both `pytest` and `unittest`.

#### Packages:
* `utils` : libraries implementing the base page model class and the browser
* `models` : libraries implementing the page models
* `tests_pytest` : tests using `pytest`
* `tests_unittest` : tests using `unittest`

#### Executing the tests

*cd into the project root*

pytest:
<br>
`python3 -m pytest tests_pytest`

unittest:
<br>
`python3 -m unittest discover tests_unittest`

Or you can run the tests in IDEs such as PyCharm.

<br>

Third-party libraries used:
* selenium
* pytest

Python version used for the development: Python 3.9.6
