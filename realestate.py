from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://www.realestate.com.au/buy')
path = "/html/body/div[1]/div[1]/div[1]/form/div[2]/div[1]/div/div/button"
search=WebDriverWait(driver,200).until(ec.element_to_be_clickable((By.XPATH, path)))
search.click()
#driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/form/div[2]/div[1]/div/div/button").click()
time.sleep(15)

images = WebDriverWait(driver,200).until(ec.presence_of_all_elements_located((By.CLASS_NAME, "property-image")))
image = len(images)
for i in range(image):
    try:
        images[i].click()
        time.sleep(5)
        p1 = "//input[@value='Price information']"
        price = WebDriverWait(driver,200).until(ec.presence_of_element_located((By.XPATH, p1)))
        price.click()

        driver.find_element_by_xpath("//input[@value='Scheduling an inspection']").click()
        driver.find_element_by_xpath("//input[@value='Price information']").click()
        driver.find_element_by_xpath("//textarea[contains(@class,'rui-input')]").send_keys("I am insterested in the property,Please Email me on ")
        driver.find_element_by_xpath("//input[@type='text']").send_keys("Ryan Dotson")
        driver.find_element_by_xpath("//input[@type='email']").send_keys("ryandotson1@hotmail.com")
        driver.find_element_by_xpath("//div[@class='contact-agent-form__mobile']//input[@type='tel']").send_keys("+16625800639")
        driver.find_element_by_xpath("//button[contains(text(),'Send')]").click()
        time.sleep(30)

        p2 = "//span[@class='rui-icon rui-icon-cross']"
        xcross = WebDriverWait(driver,200).until(ec.presence_of_element_located((By.XPATH, p2)))
        xcross.click()
        time.sleep(20)
        driver.back()
        time.sleep(40)
    except Exception:
        print("element not found")
