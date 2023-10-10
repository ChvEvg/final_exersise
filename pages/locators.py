from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_USERNAME = (By.NAME,'login-username')
    LOGIN_PASSWORD = (By.NAME,'login-password')
    REG_USERNAME = (By.NAME,'registration-email')
    REG_PASSWORD1 = (By.NAME,'registration-password1')
    REG_PASSWORD2 = (By.NAME,'registration-password2')
    LOGIN_BUTTON = (By.NAME,'login_submit')
    REG_BUTTON = (By.NAME,'registration_submit')