from selenium import webdriver;
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
binary= FirefoxBinary('F:\UniversityofDelaware\Summer2018\selenium-driver\geckodriver.exe')
browser= webdriver.Firefox();
browser.get('http://www.seleniumhq.org');

