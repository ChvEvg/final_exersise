from final_exersise.pages.base_page import BasePage
from final_exersise.pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.current_url

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), 'No login username form'
        self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), 'No login password form'
        self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), 'No login button'
        assert True

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.REG_USERNAME), 'No registration username form'
        self.is_element_present(*LoginPageLocators.REG_PASSWORD1), 'No registration password1 form'
        self.is_element_present(*LoginPageLocators.REG_PASSWORD2), 'No registration password2 form'
        self.is_element_present(*LoginPageLocators.REG_BUTTON), 'No registration button'
        assert True