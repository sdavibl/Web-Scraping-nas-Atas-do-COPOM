from driver import selecionar_elemento, selecionar_elementos
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
from time import sleep
from numpy.random import rand, randn, randint



def scrapar_ata(driver, url):
    driver.get(url)
    
    selecionar_elemento(driver, '#ataconteudo h3')
    texto_ata = driver.execute_script("""
                                        return [...document.querySelectorAll('#ataconteudo p')].map(p=>p.textContent).join('\\n')
                                        """)
    data_ata = selecionar_elemento(driver, 'div.informacoes span').text
    
    return data_ata, texto_ata


def scraping(driver):

    """ Aqui basicamente ele vai iterar sobre cada publicação do BACEN. Coloquei somente as 20 últimas publicações. """

    driver.get("https://www.bcb.gov.br/publicacoes/atascopom/cronologicos")
    atas_cupom = selecionar_elementos(driver, ".resultados-relacionados > div")
    urls = [selecionar_elemento(ata, '.btn-vermais').get_attribute('href') for ata in atas_cupom]

    datas = []
    conteudos = []

    # Antes de junho de 2020 só teremos os textos em PDF, que iremos extrair o texto em um projeto futuro
    for url in urls[0:46]:
        data, texto = scrapar_ata(driver, url)
        datas.append(data)
        conteudos.append(texto)

        # Dorme a execução por um tempo normalmente distribuído com média 7 e dp = 3
        tempo = abs(3*randn() + 7)
        sleep(tempo)
        
    return datas, conteudos