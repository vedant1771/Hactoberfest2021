from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
for i in range(20):
	driver=webdriver.Chrome()
	driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fcss%2Fhomepage.html%3Ffrom%3Dhz%26ref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
	driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys('xxxx6126')
	driver.find_element_by_xpath('//*[@id="continue"]').click()
	driver.find_element_by_xpath('//*[@id="auth-fpp-link-bottom"]').click()
	driver.find_element_by_xpath('//*[@id="continue"]').click()

	time.sleep(4)

	driver.close()
