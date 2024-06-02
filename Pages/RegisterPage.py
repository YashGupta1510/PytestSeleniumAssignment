from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Pages.BasePage import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.log = self.getLogger()

    # Text to assert
    textToAssert = (By.TAG_NAME, "b")

    # Account Details
    genderRadioField = (By.ID, "id_gender1")
    passwordTextField = (By.ID, "password")
    dayDropdownField = (By.ID, "days")
    monthDropdownField = (By.ID, "months")
    yearDropdownField = (By.ID, "years")
    newsletterCheckBoxField = (By.ID, "newsletter")
    optinCheckBoxField = (By.ID, "optin")

    # Address Details
    fnameTextField = (By.ID, "first_name")
    lnameTextField = (By.ID, "last_name")
    companyTextField = (By.ID, "company")
    address1TextField = (By.ID, "address1")
    address2TextField = (By.ID, "address2")
    countryDropdownField = (By.ID, "country")
    stateTextField = (By.ID, "state")
    cityTextField = (By.ID, "city")
    zipcodeTextField = (By.ID, "zipcode")
    mobileTextField = (By.ID, "mobile_number")

    submitButton = (By.CSS_SELECTOR, "button[type ='submit'][data-qa='create-account']")

    continueButton = (By.CSS_SELECTOR, "a[data-qa='continue-button']")
    loggedInAs = (By.PARTIAL_LINK_TEXT, " Logged in as")


    # Entering Account Details
    def select_gender(self, gender):
        self.log.info(f"Selecting Gender {gender}")
        self.driver.find_element(*RegisterPage.genderRadioField).click()

    def enter_password(self, password):
        self.log.info(f"Entering password {password}")
        self.driver.find_element(*RegisterPage.passwordTextField).send_keys(password)

    def select_day(self, day):
        self.log.info(f"Selecting Date {day}")
        select = Select(self.driver.find_element(*RegisterPage.dayDropdownField))
        select.select_by_value(day)

    def select_month(self, month):
        self.log.info(f"Selecting Month {month}")
        select = Select(self.driver.find_element(*RegisterPage.monthDropdownField))
        select.select_by_value(month)

    def select_year(self, year):
        self.log.info(f"Selecting Year {year}")
        select = Select(self.driver.find_element(*RegisterPage.yearDropdownField))
        select.select_by_value(year)

    def tick_newsletter(self):
        self.log.info(f"Ticking Checkbox for newsletter")
        element = self.driver.find_element(*RegisterPage.newsletterCheckBoxField)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.execute_script("arguments[0].click();", element)

    def tick_optin(self):
        self.log.info(f"Ticking Checkbox for optin")
        element = self.driver.find_element(*RegisterPage.optinCheckBoxField)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.execute_script("arguments[0].click();", element)


    #Entering Address Details
    def enter_fname(self, fname):
        self.log.info(f"Entering first name {fname}")
        self.driver.find_element(*RegisterPage.fnameTextField).send_keys(fname)

    def enter_lname(self, lname):
        self.log.info(f"Entering last name {lname}")
        self.driver.find_element(*RegisterPage.lnameTextField).send_keys(lname)

    def enter_company(self, company):
        self.log.info(f"Entering company name {company}")
        self.driver.find_element(*RegisterPage.companyTextField).send_keys(company)

    def enter_address1(self, address1):
        self.log.info(f"Entering address 1 {address1}")
        self.driver.find_element(*RegisterPage.address1TextField).send_keys(address1)

    def enter_address2(self, address2):
        self.log.info(f"Entering address 2 {address2}")
        self.driver.find_element(*RegisterPage.address2TextField).send_keys(address2)

    def select_country(self, country):
        self.log.info(f"Selecting country {country}")
        select = Select(self.driver.find_element(*RegisterPage.countryDropdownField))
        select.select_by_value(country)

    def enter_state(self, state):
        self.log.info(f"Entering state {state}")
        self.driver.find_element(*RegisterPage.stateTextField).send_keys(state)

    def enter_city(self, city):
        self.log.info(f"Entering city {city}")
        self.driver.find_element(*RegisterPage.cityTextField).send_keys(city)

    def enter_zipcode(self, zipcode):
        self.log.info(f"Entering zipcode {zipcode}")
        self.driver.find_element(*RegisterPage.zipcodeTextField).send_keys(zipcode)

    def enter_mobile(self, mobile):
        self.log.info(f"Entering mobile {mobile}")
        self.driver.find_element(*RegisterPage.mobileTextField).send_keys(mobile)

    def submit(self):
        element = self.driver.find_element(*RegisterPage.submitButton)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.execute_script("arguments[0].click();", element)

    def text_to_assert(self):
        return self.driver.find_element(*RegisterPage.textToAssert).text

    def fill_form(self, gender, password, day, month, year, fname, lname, company, address1, address2, country, state,
                  city, zipcode, mobile):
        self.select_gender(gender)
        self.enter_password(password)
        self.select_day(day)
        self.select_month(month)
        self.select_year(year)
        self.tick_newsletter()
        self.tick_optin()
        self.enter_fname(fname)
        self.enter_lname(lname)
        self.enter_company(company)
        self.enter_address1(address1)
        self.enter_address2(address2)
        self.select_country(country)
        self.enter_state(state)
        self.enter_city(city)
        self.enter_zipcode(zipcode)
        self.enter_mobile(mobile)
        self.submit()
        self.log.info("filled all details")

    def logout(self):
        self.log.info("Logging Out")
        self.driver.find_element(*RegisterPage.continueButton).click()

