from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = r"C:\Program Files\chromium\Bin\Chrome\chrome.exe"

driver = webdriver.Chrome(chrome_options=options)

driver.get('http://localhost:8000')

assert 'Django' in driver.title
