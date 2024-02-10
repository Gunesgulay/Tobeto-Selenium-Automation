import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from constants import globalConstants as c
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

class Test_Platform:
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

    def test_button_controls(self):
            
        self.valid_login()

        self.driver.execute_script("window.scrollTo(0,500)")

        myCourses = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, c.MY_COURSES)))
        myCourses.click()
        sleep(3)

        coursesController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, c.COURSES_CONTROLLER)))
        sleep (5)
        assert coursesController.text == "Eğitime Git"
        sleep(3)
    
        myAnnouncementsNews = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, c.NOTIFICATION)))
        myAnnouncementsNews.click()
        sleep(3)

        newsController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, c.NEWS_CONTROLLER)))
        assert newsController.text == "Duyuru"
        sleep(3)

        mySurveys = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, c.SURVEY)))
        mySurveys.click()
        sleep(3)

        surveyController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, c.SURVEY_CONTROLLER)))
        assert surveyController.text == "Atanmış herhangi bir anketiniz bulunmamaktadır"
        sleep(3)
            
        myApplications = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, c.APPLY)))
        myApplications.click()
        sleep(3)   