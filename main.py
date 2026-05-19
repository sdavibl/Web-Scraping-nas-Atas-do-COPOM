import pandas as pd
import numpy as np
from driver import criar_driver
from scraper_bcb import scraping


def main():
    with criar_driver() as driver:
        datas, conteudos = scraping(driver)
    
    df = pd.DataFrame({
            'data':datas,
            'texto':conteudos
    })

    df.to_csv("atas_copom.csv")

if __name__=="__main__":
    main()