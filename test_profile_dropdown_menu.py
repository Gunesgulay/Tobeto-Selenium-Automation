import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from constants import globalConstants as c
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

class Test_Profile_Dropdown_Menu:

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

    def test_successful_profile_information_entry(self):

        self.valid_login()
        sleep(5)
          
        clickMenu = self.driver.find_element(By.CSS_SELECTOR, c.CLICK_MENU)
        clickMenu.click()
        sleep(2)

        profileInformationButton = self.driver.find_element(By.XPATH, c.PROFILE_INFORMATION_BUTTON)
        profileInformationButton.click()
        sleep(4)
        
        birthdayInput = self.driver.find_element(By.NAME, c.BIRTHDAY_INPUT)
        birthdayInput.send_keys("19-07-1999")  

        identityNumber =self.driver.find_element(By.NAME, c.IDENTITY_NUMBER)
        identityNumber.send_keys("12345678646")
       
        countryName = self.driver.find_element(By.NAME, c.COUNTRY_NAME)
        countryName.send_keys("Türkiye")
        sleep(4)

        self.driver.execute_script("window.scrollTo(0,800)")

        city = WebDriverWait(self.driver,5).until(ec.element_to_be_clickable((By.XPATH, c.CITY)))
        city.click()

        cityName = self.driver.find_element(By.XPATH, c.CITY_NAME)
        cityName.click()
        sleep(3) 

        district = self.driver.find_element(By.NAME, c.DISTRICT)
        district.click()

        districtName = self.driver.find_element(By.XPATH, c.DISTRICT_NAME)
        districtName.click()
        sleep(3)

        enterAddress = self.driver.find_element(By.NAME, c.ADDRESS)
        enterAddress.send_keys("Misket 60 Cadde 5 No:4")
        sleep(2)
            
        aboutMe = self.driver.find_element(By.XPATH, c.ABOUT_ME)
        aboutMe.send_keys("Kendimi geliştiriyorum, yazılım testi yapmak en büyük hobim")
        sleep(3)

        saveButton = self.driver.find_element(By.XPATH, c.SAVE_BUTTON)
        saveButton.click()
        sleep(3)

        messageController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.CLASS_NAME, c.MESSAGE)))
        sleep (15)
        assert messageController.text == "• Bilgileriniz başarıyla güncellendi."
        sleep(3)

    def test_unsuccessful_profile_information_entry(self):

        self.valid_login()
        sleep(5)
          
        clickMenu = self.driver.find_element(By.CSS_SELECTOR, c.CLICK_MENU)
        clickMenu.click()
        sleep(2)

        profileInformationButton = self.driver.find_element(By.XPATH, c.PROFILE_INFORMATION_BUTTON)
        profileInformationButton.click()
        sleep(4)
        
        birthdayInput = self.driver.find_element(By.NAME, c.BIRTHDAY_INPUT)
        birthdayInput.send_keys("19-07-1999")  

        identityNumber =self.driver.find_element(By.NAME, c.IDENTITY_NUMBER)
        identityNumber.send_keys("46372843632")
       
        countryName = self.driver.find_element(By.NAME, c.COUNTRY_NAME)
        countryName.send_keys("Türkiye")

        self.driver.execute_script("window.scrollTo(0,700)")

        city = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.NAME, c.CITY)))
        sleep(3)
        city.click()

        cityName = self.driver.find_element(By.XPATH, c.CITY_NAME)
        cityName.click()
        sleep(3)

        district = self.driver.find_element(By.NAME, c.DISTRICT)
        district.click()

        districtName = self.driver.find_element(By.XPATH, c.DISTRICT_NAME)
        districtName.click()
        sleep(3)

        saveButton = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.CSS_SELECTOR, c.SAVE_BUTTON)))
        sleep(3)
        saveButton.click()
        sleep(3)

        errorMessageController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.CLASS_NAME, c.ERROR_MESSAGE_CONTROLLER)))
        assert errorMessageController.text == "• Kimlik bilgilerinizi hatalı girdiniz."
        sleep(3)    

    def test_empty_profile_information_entry(self):

        self.valid_login()
        sleep(5)
          
        clickMenu = self.driver.find_element(By.CSS_SELECTOR, c.CLICK_MENU)
        clickMenu.click()
        sleep(2)

        profileInformationButton = self.driver.find_element(By.XPATH, c.PROFILE_INFORMATION_BUTTON)
        profileInformationButton.click()
        sleep(4)

        enterName = self.driver.find_element(By.NAME, c.NAME)
        enterName.clear()

        enterSurname = self.driver.find_element(By.NAME, c.SURNAME)
        enterSurname.clear()
        
        birthdayInput = self.driver.find_element(By.NAME, c.BIRTHDAY_INPUT)
        birthdayInput.send_keys("")  

        identityNumber =self.driver.find_element(By.NAME, c.IDENTITY_NUMBER)
        identityNumber.send_keys("")
       
        countryName = self.driver.find_element(By.NAME, c.COUNTRY_NAME)
        countryName.send_keys("")

        self.driver.execute_script("window.scrollTo(0,1200)")
        sleep(7)

        saveButton = WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located((By.CSS_SELECTOR, c.SAVE_BUTTON)))
        saveButton.click()
        sleep(3)

        nameErrorMessageController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, c.NAME_ERROR_MESSAGE_CONTROLLER)))
        sleep (5)
        assert nameErrorMessageController.text == "Doldurulması zorunlu alan*"
        
        surnameErrorMessageController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, c.SURNAME_ERROR_MESSAGE_CONTROLLER)))
        sleep (5)
        assert surnameErrorMessageController.text == "Doldurulması zorunlu alan*"
        
        birthdayErrorMessageController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, c.BIRTHDAY_ERROR_MESSAGE_CONTROLLER)))
        sleep (5)
        assert birthdayErrorMessageController.text == "Doldurulması zorunlu alan*"

        identityNumberErrorMessageController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.CSS_SELECTOR, c.IDENTITY_NUMBER_ERROR_MESSAGE_CONTROLLER)))
        sleep (5)
        assert identityNumberErrorMessageController.text == "Aboneliklerde fatura için doldurulması zorunlu alan"

        countryErrorMessageController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, c.COUNTRY_ERROR_MESSAGE_CONTROLLER)))
        sleep (5)
        assert countryErrorMessageController.text == "Doldurulması zorunlu alan*"

        cityErrorMessageController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, c.CITY_ERROR_MESSAGE_CONTROLLER)))
        sleep (5)
        assert cityErrorMessageController.text == "Doldurulması zorunlu alan*"

        districtErrorMessageController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, c.DISTRICT_ERROR_MESSAGE_CONTROLLER)))
        sleep (5)
        assert districtErrorMessageController.text == "Doldurulması zorunlu alan*"

    def test_logout(self):

        self.valid_login()
        sleep(5)
          
        clickMenu = self.driver.find_element(By.CSS_SELECTOR, c.CLICK_MENU)
        clickMenu.click()
        sleep(2)  

        logoutButton = self.driver.find_element(By.XPATH, c.LOGOUT_BUTTON)  
        logoutButton.click()
        sleep(2)

        logoutController = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH, c.LOGOUT_CONTROLLER)))
        sleep (5)
        assert logoutController.text == "Giriş Yap"








        








    