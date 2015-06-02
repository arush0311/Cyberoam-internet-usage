#!/usr/bin/env python


import selenium.webdriver
from selenium.webdriver.common.keys import Keys
import time
import notify2
import getpass
print "\n\nWelcome to Cyberoam Internet Usage\nIf This is the first time you are using it Please run setup.sh first\n\n" 
username=raw_input("Username:")
password=getpass.getpass()
driver = selenium.webdriver.PhantomJS(service_args=['--ssl-protocol=tlsv1','--ignore-ssl-errors=true'])
driver.set_window_size(1124, 850)
notify2.init("INTERNET_USAGE")
while (1):
	driver.get('https://172.22.2.2/corporate/webpages/login.jsp')
        elem=driver.find_element_by_name('username')
        elem.send_keys(username)
        elem=driver.find_element_by_name('password')
        elem.send_keys(password)
        elem=driver.find_element_by_name('logintype')
        elem=elem.find_element_by_id('Language.MyAccount')
        elem.click()
        elem=driver.find_element_by_name('loginbutton')
        elem.click()
        time.sleep(5)
        elem=driver.find_elements_by_tag_name('tr')
        elem=elem[13].find_elements_by_tag_name('td')
        notify2.Notification("INTERNET USAGE","Your Remaining daily balance is " + elem[25].text).show()
        time.sleep(10)   
driver.quit();
