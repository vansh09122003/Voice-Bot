from selenium import webdriver      
from selenium.webdriver.common.keys import Keys

def searchf():
    driver=webdriver.Chrome(executable_path=r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    driver.get("https://www.google.co.in")
    assert "Google" in driver.title
    driver.click().send_keys("weather").click()

searchf()