from selenium import webdriver
import time

#opening the Browser
driver = webdriver.Firefox()

#URL to Open
driver.get('https://www.realestate.com.au/buy')

#Clicking the Search Botton to get list on properties available 

driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/form/div[2]/div[1]/div/div/button").click()
time.sleep(15)

#Click on first property image

driver.find_element_by_class_name("property-image").click()
time.sleep(5)
# Filling the Enquiry information on the page and Sending Enquiry

driver.find_element_by_xpath("//input[@value='Price information']").click()
driver.find_element_by_xpath("//input[@value='Scheduling an inspection']").click()
driver.find_element_by_xpath("//input[@value='Price information']").click()
driver.find_element_by_xpath("//textarea[contains(@class,'rui-input')]").send_keys("I am insterested in the property,Please Email me on ")
driver.find_element_by_xpath("//input[@type='text']").send_keys("Ryan Dotson")
driver.find_element_by_xpath("//input[@type='email']").send_keys("ryandotson1@hotmail.com")
driver.find_element_by_xpath("//div[@class='contact-agent-form__mobile']//input[@type='tel']").send_keys("+16625800639")
driver.find_element_by_xpath("//button[contains(text(),'Send')]").click()
time.sleep(10)
driver.find_element_by_xpath("//span[@class='rui-icon rui-icon-cross']").click()
time.sleep(2)

# To go back to the list of property 
driver.back()
