import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

chrome_options =  webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--no-sandbox")  # Required for running as root in Docker
chrome_options.add_argument("--disable-dev-shm-usage")  # Required for running in Docker
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.google.com')

driver.quit()

st.title("My app")
