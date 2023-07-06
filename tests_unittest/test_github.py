import time
import unittest

from models.github import GitHubMain
from utils.base_model import BaseModel


class TestGitHub(unittest.TestCase):
    """Test class to test the GitHub website."""

    @classmethod
    def tearDownClass(cls):
        BaseModel.close()

    def setUp(self):
        BaseModel.open('https://github.com/')

    def test_01_sign_un_enabled(self):
        """Tests if the SignUp button is enabled."""
        main_page = GitHubMain()
        time.sleep(1)
        main_page.assert_is_enabled_sign_up()

    def test_02_repo_exists(self):
        """Tests if a certain repository exists."""
        main_page = GitHubMain()
        time.sleep(1)
        main_page.click_search_disabled()
        main_page.set_search_input('rolkotaki/ml-rain-tomorrow')
        # or we could send an Enter key also instead of the next actions
        main_page.click_search_input()
        result_page = main_page.get_search_all()
        self.assertEqual(result_page.get_text_search_result(), '1 repository result')

    def test_03_login(self):
        """Tests the login feature."""
        main_page = GitHubMain()
        time.sleep(1)
        sign_in_page = main_page.get_sign_in_page()
        logged_in_page = sign_in_page.set_username('username').set_password('password').click_sign_in()
        logged_in_page.assert_is_enabled_repository_list()
