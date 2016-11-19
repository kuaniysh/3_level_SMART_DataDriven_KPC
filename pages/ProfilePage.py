from BasePage import BasePage

locators = {
  "store_tab": "xpath=//a[@title='Store' and contains(text(),'Store')]",
  "os_tab": "xpath=//span[contains(text(),'Windows')]"}

class ProfilePage(BasePage):
  def top_menu(self):
    driver = self.driver
    driver.click_element(locators['store_tab'])
    return driver.get_text(locators["os_tab"])