from utils.base_model import BaseModel


class RolkoTechProfile(BaseModel):
    locator = '//*[@id="Profile1"]/div/div/a'
    elements = {
        'profession': '//*[@id="maia-main"]/div/div[2]/table/tbody/tr[3]/td/span',
    }


class RolkoTech(BaseModel):
    locator = '//*[@id="PageList1"]/div/div[1]/div[1]/div/ul/li[1]/a'
    elements = {
        'accept_cookies': '//*[@id="cookieChoiceDismiss"]',
        'search_input': '//*[@id="BlogSearch1"]/div/form/div/input',
        'search': '/html/body/div[1]/div/div/header/div/div[3]/button',
        'first_found_article': '//*[@id="Blog1"]/div[1]/article/div/div/div[2]/div/div[1]/h1/a',
        'home_from_article': '//*[@id="Header1"]/div/div/h1/a',
        'profile': RolkoTechProfile
    }
