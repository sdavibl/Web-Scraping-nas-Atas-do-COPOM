import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import spacy
import re
from selenium import webdriver

options = webdriver.ChromeOptions()

# options.add_argument('--headless')

driver = webdriver.Chrome(options=options)

driver.get("https://www.bcb.gov.br/publicacoes/atascopom")

print(driver.title)

driver.quit()


from bs4 import BeautifulSoup
with requests.get("https://www.bcb.gov.br/publicacoes/atascopom") as req:
    soup = BeautifulSoup(req.content, 'html.parser')
