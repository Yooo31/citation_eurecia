from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import os
import time
from dotenv import load_dotenv

load_dotenv()
id = os.getenv("MAIL")
password = os.getenv("PASSWORD")

def openEurecia() :
  print('Opening eurécia website')

  driver.get("https://plateforme.eurecia.com/eurecia/logout.do")
  time.sleep(1)

def loginForm(inputType, value) :
  driver.find_element(By.ID, inputType).send_keys(os.getenv(value))
  driver.find_element(By.CSS_SELECTOR, 'button').click()

def connexion() :
  print('Start connect me')
  loginForm('email', 'MAIL')
  time.sleep(1)
  loginForm('password', 'PASSWORD')

def fillMood(citation) :
  time.sleep(20)
  driver.find_element(By.ID, 'id-smile-happy').click()
  driver.find_element(By.CSS_SELECTOR, '.ea-field__control-container textarea').send_keys(citation)


def start(citation) :
  chrome_options = Options()

  # Options to run without interface

  # chrome_options.add_argument("--no-sandbox")
  # chrome_options.add_argument("--headless")

  # Bypass the anti bot

  chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
  chrome_options.add_experimental_option('useAutomationExtension', False)
  chrome_options.add_argument("--disable-blink-features=AutomationControlled")

  # Create the driver

  global driver
  driver = webdriver.Chrome(executable_path="./chromedriver", options=chrome_options)

  # Launch the process

  openEurecia()
  connexion()
  fillMood(citation)
