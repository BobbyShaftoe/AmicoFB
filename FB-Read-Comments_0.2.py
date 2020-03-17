#!/usr/bin/env python
### sudo Xvfb :10 -ac  ### export DISPLAY=:10

import os
import re
import unittest
import pickle

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from pyvirtualdisplay import Display

os.environ['DISPLAY'] = ':1'
os.environ['G_DEBUG'] = "fatal_warnings"

display = Display(visible=0, size=(1024, 768))
display.start()

gCOOKIE = ''

evar_match = re.compile('(PATH)|(DISPLAY)|(PYTHON)')
for param in sorted(os.environ.keys()):
    if evar_match.match(param):
        print(param, os.environ[param])

firefox_capabilities = DesiredCapabilities.FIREFOX
# firefox_capabilities['marionette'] = True

print("Capabilities: ", firefox_capabilities)
print("\nDISPLAY IS ", os.environ['DISPLAY'], "\n")

facebookUserName = "minuti.jackson@gmail.com"
facebookPassword = "deepinu2"


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(capabilities=firefox_capabilities)
        self.driver.get("http://www.facebook.com")

    def test_login(self):
        driver = self.driver
        facebookUserName = "minuti.jackson@gmail.com"
        facebookPassword = "deepinu2"
        emailFieldID = "email"
        passFieldID = "pass"
        loginButtonXpath = "//input[@value='Log In']"
        fbLogoXpath = "(//a[contains(@href, 'logo')])[1]"
        emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))
        passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passFieldID))
        loginButtonElement = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_xpath(loginButtonXpath))

        emailFieldElement.clear()
        emailFieldElement.send_keys(facebookUserName)
        passFieldElement.clear()
        passFieldElement.send_keys(facebookPassword)
        loginButtonElement.click()
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(fbLogoXpath))

        with open("fb_session_cookies.pkl", "wb") as f:
            pickle.dump(driver.get_cookies(), f)
        #pickle.dump(driver.get_cookies(), open("fb_session_cookies.pkl", "wb"))
        allCookies = driver.get_cookies()
        gCOOKIE = allCookies

        pageHtml = driver.page_source
        Html_file = open("fb_page.out.html", "w")
        Html_file.write(pageHtml)
        Html_file.close()A

        # NAVIGATE TO AMICO AP
        driver.get("http://www.facebook.com/amicoapp")
        print(driver.current_url)
        #assertTrue("Not ready", not driver.current_url("False"))
        #WebDriverWait(driver, 10).until(lambda driver: driver.current_url)
        #driver.navigation.to("http://www.facebook.com/amicoapp")

        driver.save_screenshot('fb_amicoapp_page.png')
        pageHtml = driver.page_source
        Html_file = open("fb_amico_page.out.html", "w")
        Html_file.write(pageHtml)
        Html_file.close()

        print(driver.current_url)

    def tearDown(self):
        # self.browser.quit()
        display.stop()
        self.driver.quit


if __name__ == '__main__':
    verbosity = 2
    print("About to start...\n")
    print("Logging in with: ", facebookUserName)

    unittest.main()





    ###############################################################
    ### SPARE CODE/STUFF FOR RON ###

    # cookies = pickle.load(open("fb_session_cookies.pkl", "rb"))
    # for cookie in cookies:
    #    driver.add_cookie(cookie)
    # Store Session Cookie in 'fb_session_cookies.pkl'
    # Read in Session Cookie - Option
