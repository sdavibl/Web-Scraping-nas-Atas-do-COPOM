from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def criar_driver():
    """ Deixei aqui o criar driver pra facilitar a mudança de options caso eu queira"""

    options = webdriver.ChromeOptions()

    # options.add_argument('--headless')

    return webdriver.Chrome(options=options)

def selecionar_elemento(contexto, element, timeout=15, seletor = By.CSS_SELECTOR):
    wait = WebDriverWait(contexto, timeout=timeout)
    elemento = wait.until(
        EC.presence_of_element_located((seletor, element))
    )
    return elemento

def selecionar_elementos(contexto, element, timeout=15, seletor = By.CSS_SELECTOR):
    wait = WebDriverWait(contexto, timeout=timeout)
    elemento = wait.until(
        EC.presence_of_all_elements_located((seletor, element))
    )
    return elemento