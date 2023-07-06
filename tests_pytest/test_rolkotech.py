from selenium.webdriver.common.keys import Keys

from models.rolkotech import RolkoTech
from utils.base_model import BaseModel


class TestRolkoTech:
    """Test class to test the RolkoTech website."""

    @classmethod
    def setup_class(cls):
        BaseModel.open('https://rolkotech.blogspot.com/')

    @classmethod
    def teardown_class(cls):
        BaseModel.close()

    def test_01_accept_cookies(self):
        """Tests accepting the cookies."""
        main_page = RolkoTech()
        main_page.click_accept_cookies()

    def test_02_mojo_article_exits(self):
        """Tests if the article about Mojo exists."""
        main_page = RolkoTech()
        main_page.set_search_input('mojo', send_key=Keys.ENTER)
        main_page.click_first_found_article()
        main_page.click_home_from_article()

    def test_03_profession(self):
        """Test and verifies the profession of the blog author."""
        main_page = RolkoTech()
        profile_page = main_page.get_profile()
        assert profile_page.get_text_profession() == 'Software Engineer'
