import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin(unittest.TestCase): # test scenario

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_success1_login(self): #test cases 1 (Login sukses dan tampilan produk sesuai)
        Url = "https://www.saucedemo.com"
        driver = self.browser
        driver.get(Url)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys("secret_sauce")
        driver.find_element(By.NAME, "login-button").click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, Url + "/inventory.html")

    def test_success2_login(self): #test cases 2 (Login sukses, namun tampilan produk tidak sesuai)
        Url = "https://www.saucedemo.com"
        driver = self.browser
        driver.get(Url)
        driver.find_element(By.ID, "user-name").send_keys("problem_user")
        driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys("secret_sauce")
        driver.find_element(By.NAME, "login-button").click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, Url + "/inventory.html")

    def test_failed1_login(self): #test cases 3 (Login gagal, username dan password tidak diisi)
        Url = "https://www.saucedemo.com"
        driver = self.browser
        driver.get(Url)
        driver.find_element(By.NAME, "login-button").click()
        error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        self.assertIn("Epic sadface: Username is required", error_message)

    def test_failed2_login(self): #test cases 4 (Login gagal, password tidak diisi)
        Url = "https://www.saucedemo.com"
        driver = self.browser
        driver.get(Url)
        driver.find_element(By.ID, "user-name").send_keys("haitest")
        driver.find_element(By.NAME, "login-button").click()
        error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        self.assertIn("Epic sadface: Password is required", error_message)

if __name__ == '__main__':
    unittest.main()