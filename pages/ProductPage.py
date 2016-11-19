from BasePage import BasePage

locators = {
  "os_tab": "xpath=//span[contains(text(),'Windows')]",
  "product_tab": "xpath=//*[contains(@class,'header-submenu-title')][text()='Windows']/..//a[contains(@title,'{}')]",
  "first_data": "xpath=//*[@id='storeContent']//tr/td[1]",
  "second_data": "xpath=//*[@id='storeContent']//tr/td[2]",
  "third_data": "xpath=//*[@id='storeContent']//table//span[@itemprop='price']",
  "user_email": "xpath=//span[@class='user-email']"}


class ProductPage(BasePage):
  def check_product(self, tab):
    driver = self.driver
    driver.click_element(locators['os_tab'])
    driver.click_element(locators['product_tab'].format(tab))
    first_data = driver.get_text(locators['first_data'])
    second_data = driver.get_text(locators['second_data'])
    third_data = driver.get_text(locators['third_data'])
    all_data = first_data + " " + second_data + " " + third_data
    return all_data