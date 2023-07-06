from selenium import webdriver


def create_browser(url=None):
    """Creates a new Chrome browser and navigates to the passed URL if any."""
    browser = webdriver.Chrome()
    if url:
        browser.get(url)
    return browser
