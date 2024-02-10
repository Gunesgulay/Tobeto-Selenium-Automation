import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from constants import globalConstants as c
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

class Test_Platform_Menu_Bar:
    
    def setup_method(self):

        chrome_driver_path = Service("/Users/gunesgulay/Downloads/chromedriver-mac-arm64/chromedriver")
        self.driver = webdriver.Chrome(service=chrome_driver_path)
        self.driver.get(c.LOGIN_URL)
        self.driver.maximize_window()

    def teardown_method(self):

        self.driver.quit()  

    def valid_login(self):

        firstLoginButton = self.driver.find_element(By.CSS_SELECTOR,c.FIRST_LOGIN_BUTTON)
        firstLoginButton.click()

        emailInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.EMAIL_NAME)))
        emailInput.send_keys("majajiv633@vasteron.com")

        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.PASSWORD_NAME)))
        passwordInput.send_keys("deneme123")

        loginButton = self.driver.find_element(By.XPATH,c.LOGIN_BUTTON_XPATH)
        loginButton.click()

        loginMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,c.LOGIN_MESSAGE_CSS)))
        assert loginMessage.text == "• Giriş başarılı."    
    
  
    def test_menu_bar_ikon(self):
            
        self.valid_login()    
            
        homePageButton = self.driver.find_element(By.XPATH, c.HOME_PAGE)
        homePageButton.click()
        sleep(2)

        homePageController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.CSS_SELECTOR, c.HOME_PAGE_CONTROLLER)))
        assert homePageController.text == "TOBETO'ya hoş geldin"
        sleep(3)
            
        myProfileButton = self.driver.find_element(By.XPATH, c.MY_PROFILE)
        myProfileButton.click()
        sleep(3)

        profileController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, c.MY_PROFILE_CONTROLLER)))
        assert profileController.text == "test automation"
        sleep(3)

        assessmentsButton = self.driver.find_element(By.XPATH, c.ASSESSMENTS)
        assessmentsButton.click()
        sleep(3)

        assessmentsController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, c.ASSESSMENTS_CONTROLLER)))
        assert assessmentsController.text == "Yetkinliklerini ücretsiz ölç, bilgilerini test et."
        sleep(3)

        catalogButton = self.driver.find_element(By.XPATH, c.CATALOG)
        catalogButton.click()
        sleep(3)

        catalogController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, c.CATALOG_CONTROLLER)))
        assert catalogController.text == "Öğrenmeye başla !"
        sleep(3)

        calendarButton = self.driver.find_element(By.XPATH, c.CALENDAR)
        calendarButton.click()
        sleep(3)

        calendarController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.CSS_SELECTOR, c.CALENDAR_CONTROLLER)))
        assert calendarController.text == "Bugün"
        sleep(3)
            
        istanbulCodingButton = self.driver.find_element(By.XPATH, c.ISTANBUL_CODING)
        istanbulCodingButton.click()
        sleep(3)

        istanbulCodingController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.CSS_SELECTOR, c.ISTANBUL_CODING_CONTROLLER)))
        assert istanbulCodingController.text == "Aradığın  “İş”  Burada!"
        sleep(3)


            