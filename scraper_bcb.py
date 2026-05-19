from driver import selecionar_elemento, selecionar_elementos
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def scrapar_ata(driver, elemento):
    ver_mais = selecionar_elemento(elemento, '.btn-vermais')
    driver.execute_script("arguments[0].click()", ver_mais)
    
    texto_ata = selecionar_elemento(driver, '#ataconteudo').text
    data_ata = selecionar_elemento(driver, 'div.informacoes span').text
    
    return data_ata, texto_ata


def scraping(driver, n=20):

    """ Aqui basicamente ele vai iterar sobre cada publicação do BACEN. Coloquei somente as 20 últimas publicações. """

    driver.get("https://www.bcb.gov.br/publicacoes/atascopom/cronologicos")
    atas_cupom = selecionar_elementos(driver, ".resultados-relacionados > div")

    datas = []
    conteudos = []

    for ata in atas_cupom[0:n]:
        data, texto = scrapar_ata(driver, ata)
        datas.append(data)
        conteudos.append(texto)
        driver.get("https://www.bcb.gov.br/publicacoes/atascopom/cronologicos")
    return 0