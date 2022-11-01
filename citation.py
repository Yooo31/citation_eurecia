from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def open_website():
  print('Opening web site')

  driver.get("http://evene.lefigaro.fr/citations/mot.php?mot=jour")
  time.sleep(200)



def start() :
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

  open_website()
  # accept_cookies()
