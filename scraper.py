import requests
import time
import random
from bs4 import BeautifulSoup, element
from selenium import webdriver

link = 'https://www.linkedin.com/in/satyanadella/'

browser = webdriver.Chrome('./chromedriver')
browser.get('https://www.linkedin.com/uas/login')
file = open('config.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]

elementID = browser.find_element_by_id('username')
elementID.send_keys(username)

elementID = browser.find_element_by_id('password')
elementID.send_keys(password)

elementID.submit()

browser.get(link)

SCROLL_PHASE_TIME = 5

last_height = browser.execute_script("return document.body.scrollHeight")

for i in range(3):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight); ")

    time.sleep(SCROLL_PHASE_TIME)

    new_height = browser.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        break

    last_height = new_height
