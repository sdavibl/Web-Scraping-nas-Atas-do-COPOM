from bs4 import BeautifulSoup
import requests

from bs4 import BeautifulSoup
with requests.get("https://www.bcb.gov.br/publicacoes/atascopom") as req:
    soup = BeautifulSoup(req.content, 'html.parser')
