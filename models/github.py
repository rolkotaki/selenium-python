from utils.base_model import BaseModel


class GitHubLoggedInMain(BaseModel):
    locator = '//*[@id="login"]/div[4]/form/div/input[13]'
    elements = {
        'repository_list': '/html/body/div[1]/div[6]/div/div/aside/div/loading-context/div/div[1]/div/ul',
    }


class GitHubLogin(BaseModel):
    locator = '//a[contains(., "Sign in")]'
    elements = {
        'username': '//*[@id="login_field"]',
        'password': '//*[@id="password"]',
        'sign_in': GitHubLoggedInMain,
    }


class GitHubSearchResults(BaseModel):
    locator = '//*[@id="jump-to-suggestion-search-global"]/a/div[3]'
    elements = {
        'search_result': '/html/body/div[1]/div[4]/main/div/div[3]/div/div[2]/h3',
    }


class GitHubMain(BaseModel):
    locator = '/html/body/div[1]/div[1]/header/div/div[1]/a'
    elements = {
        'sign_in_page': GitHubLogin,
        'sign_up': '/html/body/div[1]/div[1]/header/div/div[2]/div/div/a',
        'search_disabled': '/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label',
        'search_input': '/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label/input[1]',
        'search_all': GitHubSearchResults,
    }
