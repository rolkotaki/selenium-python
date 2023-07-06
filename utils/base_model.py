from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

from utils.browser import create_browser


class BaseModel(object):
    """The BaseModel class represents a page model that knows its locator and its elements.
    It is capable of several operations with its elements, such as get, set, click or assert.
    BaseModel has a browser that is used by all of its instances.
    """
    browser = None
    locator = ''

    @classmethod
    def __set_browser(cls, url):
        """Creates a new browser and navigates to the passed URL if any."""
        if not BaseModel.browser:
            BaseModel.browser = create_browser(url)

    @classmethod
    def open(cls, url):
        """Creates a browser if not yet done and navigates to the passed URL."""
        if cls.browser:
            cls.browser.get(url)
        else:
            cls.__set_browser(url)

    @classmethod
    def close(cls):
        """Closes and deletes the browser."""
        if cls.browser:
            cls.browser.quit()
            cls.browser = None

    def __init__(self):
        if not hasattr(self, 'locator'):
            return
        if not BaseModel.browser:
            return
        self.click()

    def click(self):
        """Clicks on the locator of the model. Called from the constructor."""
        self.browser.find_element(by=By.XPATH, value=self.locator).click()

    def __getattr__(self, item):
        """Customizing the __getattr__ function so that we can return and call the right method of the class
        when we call a customized method name on the class.
        For example, calling click_login will call the click_element method and pass 'login' as the parameter,
        which refers to the element name.
        """

        def wrapper(*args, **kwargs):
            if item.startswith('click_'):
                return self.click_element(item[6:])
            if item.startswith('get_text_'):
                return self.get_element_text(item[9:])
            if item.startswith('get_'):
                return self.get_element(item[4:])
            if item.startswith('set_'):
                return self.set_element_value(item[4:], *args, **kwargs)
            if item.startswith('assert_is_enabled'):
                return self.assert_is_enabled(item[18:])
            if item.startswith('assert_not_enabled'):
                return self.assert_not_enabled(item[19:])

        if item.startswith(('set_', 'get_', 'click_', 'assert_is_enabled_', 'assert_not_enabled_')):
            return wrapper
        else:
            raise AttributeError("'%s' instance has no attribute '%s'" % (self.__class__.__name__, item))

    def __get_locator(self, element_name):
        """Returns the locator (XPATH) of an element of the model."""
        if element_name not in self.elements.keys():
            raise AttributeError("{} model has no element {}".format(self.__class__.__name__, element_name))
        locator = self.elements[element_name]
        if isinstance(locator, BaseModel) or (type(locator) == type and issubclass(locator, BaseModel)):
            return locator
        return locator

    def get_element(self, element_name):
        """Returns an element of the page or a new page model if the locator is a model class."""
        locator_or_class = self.__get_locator(element_name)
        if isinstance(locator_or_class, str):
            ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
            element = WebDriverWait(self.browser, 10, ignored_exceptions=ignored_exceptions) \
                .until(expected_conditions.presence_of_element_located((By.XPATH, locator_or_class)))
            return element
        else:
            return locator_or_class()

    def get_element_text(self, element_name):
        """Returns the text of an element of the page."""
        locator_or_class = self.__get_locator(element_name)
        if isinstance(locator_or_class, str):
            return self.get_element(element_name).text
        return None

    def click_element(self, element_name):
        """Clicks on an element of the page or if the element is a model class, clicks on its locator."""
        locator_or_class = self.__get_locator(element_name)
        if isinstance(locator_or_class, str):
            element = self.get_element(element_name)
            ActionChains(self.browser).move_to_element(element).perform()
            WebDriverWait(self.browser, 10).until(expected_conditions.element_to_be_clickable(
                                                            (By.XPATH, locator_or_class)))
            element.click()
        else:
            return locator_or_class()
        return self

    def set_element_value(self, element_name, value, **kwargs):
        """Sets the text value of an element such as an input text field."""
        locator_or_class = self.__get_locator(element_name)
        if isinstance(locator_or_class, str):
            element = self.get_element(element_name)
            ActionChains(self.browser).move_to_element(element).perform()
            element.clear()
            element.send_keys(value)
            if 'send_key' in kwargs.keys():
                element.send_keys(kwargs.get('send_key'))
            return self

    def assert_is_enabled(self, element_name):
        """Asserts if en element of the page is enabled."""
        assert self.get_element(element_name).is_enabled(), '{} is not enabled'.format(element_name)

    def assert_not_enabled(self, element_name):
        """Asserts if en element of the page is not enabled."""
        assert not self.get_element(element_name).is_enabled(), '{} is enabled'.format(element_name)
