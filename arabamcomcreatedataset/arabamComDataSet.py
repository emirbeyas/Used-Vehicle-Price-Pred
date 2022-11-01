from cgitb import text
from lib2to3.pgen2 import driver
from urllib.request import AbstractBasicAuthHandler
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.chrome.options import Options
import Ilan

import arabamcomdataset.DbContext as DbContext

driverPath = "C:\ChromeDriver\chromedriver.exe"

option = Options()

option.add_argument('--disable-notifications')

driver = webdriver.Chrome(executable_path= driverPath, chrome_options= option)

# https://www.arabam.com/ikinci-el/otomobil/alfa-romeo-147?days=1&take=50
# https://www.arabam.com/ikinci-el/otomobil/audi?days=1&take=50&page=2
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# def ilanLinkleriBul():

linkBasi = "https://www.arabam.com/ikinci-el/"
kategoriler = ["otomobil/", "arazi-suv-pick-up/", "minivan-van_panelvan/"]
aracMarkalar = []
aracMarkaModeller = []
ilanLinkler = []
elliArac = "?take=50"
sayfa = "&page="
sonYirmiDort = "?days=1"

for kategori in kategoriler:
    aracMarkalariCek = True
    driver.get(linkBasi + kategori.replace("/","") + sonYirmiDort)
    time.sleep(1)

    if aracMarkalariCek:
        aracMarkalari = driver.find_elements(by=By.CSS_SELECTOR, value=".scrollable-category > .ss-wrapper > .ss-content > div > ul")
        aracMarkalariCek = False
        
    for aracMarka in aracMarkalari:
        aracMarkalar.append(aracMarka.text.split("(")[0].strip().lower().replace(" ", "-").replace("ş", "s"))
    
    aracMarkalar.remove("mercedes---benz")
    aracMarkalar.append("mercedes-benz")

    for aracMarka in aracMarkalar:
        driver.get(linkBasi + kategori + aracMarka + sonYirmiDort)
        time.sleep(1)
        aracModeller = driver.find_elements(by= By.CSS_SELECTOR, value= ".scrollable-category > .ss-wrapper > .ss-content > div > ul")
        
        for aracModel in aracModeller:
            aracMarkaModeller.append(aracModel.text.split("(")[0].strip().lower().replace(" ", "-"))
            
        for aracModeli in aracMarkaModeller:
            driver.get(linkBasi + kategori + aracMarka + "-" + aracModeli + sonYirmiDort + elliArac)
            time.sleep(1)

            try:
                ilanSayisi = int(driver.find_element(by= By.CSS_SELECTOR, value= "#js-hook-missing-space-content > .selected-filters-wrapper > #top-bar > div > div:nth-child(1) > span > span").text.strip().replace(".",""))
                # sayfaSayisi = int(ilanSayisi / 50) + 1
                sayfaSayisi = 50 if (int(ilanSayisi / 50) + 1) > 50 else (int(ilanSayisi / 50) + 1)
            except:
                sayfaSayisi = 1
        
            for i in range (sayfaSayisi):
                if i > 0:
                    driver.get(linkBasi + kategori + aracMarka + "-" + aracModeli + sonYirmiDort + elliArac + sayfa + str(i+1))
                    time.sleep(1)
                sayfadakiIlanlar = driver.find_elements(by=By.CSS_SELECTOR, value=".listing-content-container > table > tbody > tr")
                
                for i in range(len(sayfadakiIlanlar)):
                    try:
                        ilanLinkler.append(driver.find_element(by=By.CSS_SELECTOR, value=".listing-content-container > table > tbody > tr:nth-child(" + str(i+1) + ") > td:nth-child(1) > .fade-out-content-wrapper > a").get_attribute('href'))
                        # ilanLink = driver.find_element(by=By.CSS_SELECTOR, value=".listing-content-container > table > tbody > tr:nth-child(" + str(i+1) + ") > td:nth-child(1) > .fade-out-content-wrapper > a").get_attribute('href')
                        # DbContext.addIlanLink(ilanLink)
                        # print(kategori)
                    except:
                        print("a Etiketine Ulaşılamadı.")
                for i in ilanLinkler:
                    Ilan.ilanDetaylar(i)
                ilanLinkler.clear()

        aracMarkaModeller.clear()

    aracMarkalar.clear()

    
    # return ilanLinkler

