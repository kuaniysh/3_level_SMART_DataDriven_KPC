from BasePage import BasePage

locators = {
  "sign_in_button": "//button[contains(., 'Sign in')]",
  "email_field": "xpath=//div[@class='modal']//form//input[@name='EMail']",
  "password_field": "xpath=//div[@class='modal']//form//input[@name='Password']",
  "submit_button": "xpath=//div[@class='modal']//form//button[text()='Sign in']",
  "user_email": "xpath=//span[@class='user-email']"}



class MainPage(BasePage):
  def login(self, email, password):
    driver = self.driver
    driver.click_element(locators["sign_in_button"])
    driver.input_text(locators["email_field"], email)
    driver.input_text(locators["password_field"], password)
    driver.click_element(locators["submit_button"])
    driver.wait_until_element_is_visible(locators["user_email"], 10)
    return driver.get_text(locators["user_email"])
