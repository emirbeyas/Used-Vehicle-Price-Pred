from cgitb import text
from lib2to3.pgen2 import driver
from operator import is_not
from urllib.request import AbstractBasicAuthHandler
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import arabamcomdataset.DbContext as DbContext
import time 

driverPath = "C:\ChromeDriver\chromedriver.exe"

option = Options()

option.add_argument('--disable-notifications')

driver = webdriver.Chrome(executable_path= driverPath, chrome_options= option)


# def boyaDegisenStrToInt(durum):
#     if durum == "Orijinal":
#         return "1"
#     elif durum == "Boyanmış":
#         return "2"
#     elif durum == "Lokal Boyanmış":
#         return "3"
#     elif durum == "Değişmiş":
#         return "4"
#     else:
#         return "0"

def ilanDetaylar(ilanLinkler):

    # for ilan in ilanLinkler:
        
        ilanNo = ""
        marka = ""
        seri = ""
        model = ""
        yil = ""
        km = ""
        vites = ""
        yakit = ""
        kasa = ""
        motorHacim = ""
        motorGucu = ""
        aciklama = ""
        toplamTramer = ""
        sagArkaCamurluk = "0"
        arkaKaput = "0"
        solArkaCamurluk = "0"
        sagArkaKapi = "0"
        sagOnKapi = "0"
        tavan = "0"
        solArkaKapi = "0"
        solOnKapi = "0"
        sagOnCamurluk = "0"
        motorKaputu = "0"
        solOnCamurluk = "0"
        onTampon = "0"
        arkaTampon = "0"
        agirHasar = "0"
        
        driver.get(ilanLinkler)
        # driver.get(ilan)
        
        try:
            ilanDetay = driver.find_elements(by=By.CSS_SELECTOR, value="#js-hook-for-observer-detail > .banner-column-detail > ul > li")

            for i in ilanDetay:
                if i.text.split(":")[0].strip() == "İlan No":
                    ilanNo = i.text.split(":")[1].strip()
                elif i.text.split(":")[0].strip() == "Marka":
                    marka = i.text.split(":")[1].strip()
                elif i.text.split(":")[0].strip() == "Seri":
                    seri = i.text.split(":")[1].strip()
                elif i.text.split(":")[0].strip() == "Model":
                    model = i.text.split(":")[1].strip()
                elif i.text.split(":")[0].strip() == "Yıl":
                    yil = i.text.split(":")[1].strip()
                elif i.text.split(":")[0].strip() == "Kilometre":
                    km = i.text.split(":")[1].strip()
                elif i.text.split(":")[0].strip() == "Vites Tipi":
                    vites = i.text.split(":")[1].strip()
                elif i.text.split(":")[0].strip() == "Yakıt Tipi":
                    yakit = i.text.split(":")[1].strip()
                elif i.text.split(":")[0].strip() == "Kasa Tipi":
                    kasa = i.text.split(":")[1].strip()
                elif i.text.split(":")[0].strip() == "Motor Hacmi":
                    motorHacim = i.text.split(":")[1].strip()
                elif i.text.split(":")[0].strip() == "Motor Gücü":
                    motorGucu = i.text.split(":")[1].strip()
                    
            # ilanNo = driver.find_element(by=By.CSS_SELECTOR, value="#js-hook-for-observer-detail > .banner-column-detail > ul > li:nth-child(1)").text.split(":")[1].strip()
            # marka = driver.find_element(by=By.CSS_SELECTOR, value="#js-hook-for-observer-detail > .banner-column-detail > ul > li:nth-child(3)").text.split(":")[1].strip()
            # seri = driver.find_element(by=By.CSS_SELECTOR, value="#js-hook-for-observer-detail > .banner-column-detail > ul > li:nth-child(4)").text.split(":")[1].strip()
            # model = driver.find_element(by=By.CSS_SELECTOR, value="#js-hook-for-observer-detail > .banner-column-detail > ul > li:nth-child(5)").text.split(":")[1].strip()
            # yil = driver.find_element(by=By.CSS_SELECTOR, value="#js-hook-for-observer-detail > .banner-column-detail > ul > li:nth-child(6)").text.split(":")[1].strip()
            # km = driver.find_element(by=By.CSS_SELECTOR, value="#js-hook-for-observer-detail > .banner-column-detail > ul > li:nth-child(7)").text.split(":")[1].strip()
            # vites = driver.find_element(by=By.CSS_SELECTOR, value="#js-hook-for-observer-detail > .banner-column-detail > ul > li:nth-child(8)").text.split(":")[1].strip()
            # yakit = driver.find_element(by=By.CSS_SELECTOR, value="#js-hook-for-observer-detail > .banner-column-detail > ul > li:nth-child(9)").text.split(":")[1].strip()
            # kasa = driver.find_element(by=By.CSS_SELECTOR, value="#js-hook-for-observer-detail > .banner-column-detail > ul > li:nth-child(10)").text.split(":")[1].strip()
            # motorHacim = driver.find_element(by=By.CSS_SELECTOR, value="#js-hook-for-observer-detail > .banner-column-detail > ul > li:nth-child(11)").text.split(":")[1].strip()
            # motorGucu = driver.find_element(by=By.CSS_SELECTOR, value="#js-hook-for-observer-detail > .banner-column-detail > ul > li:nth-child(12)").text.split(":")[1].strip()

            fiyat = driver.find_element(by=By.CSS_SELECTOR, value="#js-hook-for-observer-detail > .banner-column-detail > div:nth-child(1) > div:nth-child(1) > .color-red4 ").text.strip()

        except:
            print("ilan Detaylarına Ulaşılamadı")    
        try:
            aciklama = driver.find_element(by=By.CSS_SELECTOR, value="#js-hook-for-observer-aciklama > #js-hook-description > div").text
        except:
            print("Tramer Bilgisi Yok")
        
        try:
            boyaDegisen = driver.find_elements(by=By.CSS_SELECTOR, value="#js-hook-for-observer-boyadegisen > div > div:nth-child(2) > ul:nth-child(1) > li")

            for i in boyaDegisen:
                if i.text.split(":")[0] == "Sağ Arka Çamurluk":
                    sagArkaCamurluk = i.text.split(":")[1].strip()
                elif i.text.split(":")[0] == "Arka Kaput":
                    arkaKaput = i.text.split(":")[1].strip()
                elif i.text.split(":")[0] == "Sol Arka Çamurluk":
                    solArkaCamurluk = i.text.split(":")[1].strip()
                elif i.text.split(":")[0] == "Sağ Arka Kapı":
                    sagArkaKapi = i.text.split(":")[1].strip()
                elif i.text.split(":")[0] == "Sağ Ön Kapı":
                    sagOnKapi = i.text.split(":")[1].strip()
                elif i.text.split(":")[0] == "Tavan":
                    tavan = i.text.split(":")[1].strip()
                elif i.text.split(":")[0] == "Sol Arka Kapı":
                    solArkaKapi = i.text.split(":")[1].strip()
                elif i.text.split(":")[0] == "Sol Ön Kapı":
                    solOnKapi = i.text.split(":")[1].strip()
                elif i.text.split(":")[0] == "Sağ Ön Çamurluk":
                    sagOnCamurluk = i.text.split(":")[1].strip()
                elif i.text.split(":")[0] == "Motor Kaputu":
                    motorKaputu = i.text.split(":")[1].strip()
                elif i.text.split(":")[0] == "Sol Ön Çamurluk":
                    solOnCamurluk = i.text.split(":")[1].strip()
                elif i.text.split(":")[0] == "Ön Tampon":
                    onTampon = i.text.split(":")[1].strip()
                elif i.text.split(":")[0] == "Arka Tampon":
                    arkaTampon = i.text.split(":")[1].strip()
                else:
                    print("boya Degisen Bilgisi Yok")
        except:
            print("boya Degisen Bilgisi Yok")
        tramer = ""
        try:
            tramer = driver.find_element(by=By.CSS_SELECTOR, value="#js-hook-for-observer-boyadegisen > div > div:nth-child(3)").text
            
            toplamTramer = tramer.split(":")[1].strip()
        except:
            print("Tramer Bilgisi Yok")
            toplamTramer = "-1 TL"
        try:
            if (tramer.strip()) == "Tramer tutarı yok":
                toplamTramer = "0 TL"
            if (tramer.strip()) == "Bu araç ağır hasar kayıtlıdır.":
                agirHasar = "1"
        except:
            toplamTramer = "-1 TL"

        if ilanNo != "":
            
            DbContext.addAdvert(ilanNo, marka, seri, model, yil, km, vites, yakit, kasa, motorHacim, motorGucu, aciklama, toplamTramer, fiyat, sagArkaCamurluk, arkaKaput, solArkaCamurluk, sagArkaKapi, sagOnKapi, tavan, solArkaKapi, solOnKapi, sagOnCamurluk, motorKaputu, solOnCamurluk, onTampon, arkaTampon, agirHasar)


