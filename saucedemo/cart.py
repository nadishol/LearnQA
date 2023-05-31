import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin(unittest.TestCase): # test scenario

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_Add_cart(self): #test cases 1 (Tambahkan produk ke keranjang)
        Url = "https://www.saucedemo.com"
        driver = self.browser
        driver.get(Url)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys("secret_sauce")
        driver.find_element(By.NAME, "login-button").click()
        driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-bike-light']").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, Url + "/cart.html")


if __name__ == '__main__':
    unittest.main()