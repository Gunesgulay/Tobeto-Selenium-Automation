from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
import openpyxl
from time import sleep
from constants import globalConstants as c
from selenium.webdriver.common.action_chains import ActionChains

class Test_Registerclass:

    def setup_method(self):
        chrome_driver_path = Service("/Users/gunesgulay/Downloads/chromedriver-mac-arm64/chromedriver")
        self.driver = webdriver.Chrome(service=chrome_driver_path)
        self.driver.get(c.BASE_URL)
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()  

    def successful_register(self, phone):

        firstRegisterButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,c.FIRST_REGISTER_BUTTON)))
        firstRegisterButton.click()

        nameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.NAME_NAME)))
        nameInput.send_keys("python")

        surnameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.SURNAME_NAME)))
        surnameInput.send_keys("language")

        enterEmail = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.ENTER_EMAIL)))
        enterEmail.send_keys("testautomation652@gmail.com")

        enterPassword = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.ENTER_PASSWORD)))
        enterPassword.send_keys("deneme123") 

        passwordAgain = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.PASSWORD_AGAIN)))
        passwordAgain.send_keys("deneme123") 
        sleep (5)

        registerButton = WebDriverWait(self.driver,15).until(ec.visibility_of_element_located((By.XPATH,c.REGISTER_BUTTON_XPATH)))
        sleep (5)
        registerButton.click() 

        explicitConsentStatementCheckbox = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.EXPLICIT_CONSENT_CHECKBOX)))
        explicitConsentStatementCheckbox.click()

        membershipContratCheckbox = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.MEMBERSHIP_CONTRAT_CHECKBOX)))
        membershipContratCheckbox.click()

        emailConfirmationCheckbox = self.driver.find_element(By.NAME,c.EMAIL_CONFIRMATION_CHECKBOX)
        emailConfirmationCheckbox.click()

        phoneConfirmationCheckbox = self.driver.find_element(By.NAME,c.PHONE_CONFIRMATION_CHECKBOX)
        phoneConfirmationCheckbox.click()

        enterPhone = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,c.ENTER_PHONE)))
        enterPhone.send_keys(phone)

        iframe = self.driver.find_element(By.XPATH,c.IFRAME_XPATH)
        self.driver.switch_to.frame(iframe)
        sleep (2)

        reCAPTCHA = self.driver.find_element(By.XPATH, c.RECAPTCHA_CHECKBOX)
        reCAPTCHA.click()

        self.driver.switch_to.default_content()

        continueButton = self.driver.find_element(By.CSS_SELECTOR,c.CONTINUE_BUTTON_CSS)
        continueButton.click()

    def test_successful_register(self):

        self.successful_register("5068414863")

        registerMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,c.REGISTER_MESSAGE)))
        assert registerMessage.text == "Tobeto Platform'a kaydınız başarıyla gerçekleşti."
 
    def test_invalid_email(self):

        firstRegisterButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,c.FIRST_REGISTER_BUTTON)))
        firstRegisterButton.click()

        enterEmail = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME,c.ENTER_EMAIL)))
        enterEmail.send_keys("testautomation652@")
        
        invalidEmailMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,c.INVALID_EMAIL_MESSAGE)))
        assert invalidEmailMessage.text == "Geçersiz e-posta adresi*"    

    def test_invalid_phone_message(self):

        self.successful_register("1234")

        invalidPhoneMessage = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,c.INVALID_PHONE_MESSAGE)))
        assert invalidPhoneMessage.text == "En az 10 karakter girmelisiniz."

    def test_invalid_phone_message2(self):

        self.successful_register("12345678987")

        invalidPhoneMessage2 = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,c.INVALID_PHONE_MESSAGE2)))
        assert invalidPhoneMessage2.text == "En fazla 10 karakter girmelisiniz."    