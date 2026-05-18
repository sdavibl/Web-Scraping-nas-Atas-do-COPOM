import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import spacy
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from nlp import lemmetizador

def abrirSelenium():
    options = webdriver.ChromeOptions()

    # Vamos deixar o navegador invisível
    # options.add_argument('--headless')

    with webdriver.Chrome(options=options) as driver:
        scraping(driver)


def scraping(driver):
    driver.get("https://www.bcb.gov.br/publicacoes/atascopom")
    texto = driver.find_element(By.CSS_SELECTOR, "#ataconteudo").text
    print("...")

if __name__=="__main__":
    abrirSelenium()