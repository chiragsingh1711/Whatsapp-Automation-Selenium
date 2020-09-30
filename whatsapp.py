from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from pynput.keyboard import Key, Controller


chromedriver="F:\Python 3.8.3\chromedriver_win32\chromedriver"
driver=webdriver.Chrome(chromedriver)
keyboard=Controller()

driver.get('https://web.whatsapp.com/')
time.sleep(10)
driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]').click()
time.sleep(1)
for i in range(1,20):
    keyboard.type("Good night")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
