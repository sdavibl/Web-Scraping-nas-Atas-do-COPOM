import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import spacy
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from nlp import lemmetizador
from driver import criar_driver, selecionar_elemento
from scraper_bcb import scraping

def main():
    with criar_driver() as driver:
        scraping(driver)
    return 0

if __name__=="__main__":
    main()