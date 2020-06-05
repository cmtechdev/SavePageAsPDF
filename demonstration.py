from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from SavePageAsPDF import *

driver = webdriver.Firefox()
driver.get("http://www.python.org")
SavePageAsPDF( driver, 'pdfName.pdf' )
driver.quit()