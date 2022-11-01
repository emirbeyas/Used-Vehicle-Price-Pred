
import re
import pandas as pd
import numpy as np
import pypyodbc
import DbContext as db

def seriListele(marka):
    aracbilgiler = db.getInfoWithMarka(marka)
    df = pd.DataFrame(aracbilgiler)
    df.rename(columns={0: 'marka', 1: 'seri', 2: 'paket', 3: 'yil', 4: 'vites', 5: 'yakit', 6: 'kasa'}, inplace=True)
    return np.sort(df["seri"].unique()).tolist()

def yilListele(marka, seri):
    aracbilgiler = db.getInfoWithMarkaAndSeri(marka, seri)
    df = pd.DataFrame(aracbilgiler)
    df.rename(columns={0: 'marka', 1: 'seri', 2: 'paket', 3: 'yil', 4: 'vites', 5: 'yakit', 6: 'kasa'}, inplace=True)
    return np.sort(df["yil"].unique()).tolist()

def paketListele(marka, seri, yil):
    aracbilgiler = db.getInfoWithMarkaAndSeriAndYil(marka , seri, yil)
    df = pd.DataFrame(aracbilgiler)
    df.rename(columns={0: 'marka', 1: 'seri', 2: 'paket', 3: 'yil', 4: 'vites', 5: 'yakit', 6: 'kasa'}, inplace=True)
    return df["paket"].unique().tolist()

def aracBilgiListele(marka, seri, yil, paket):
    liste = []
    motorHacimList = []
    motorGucuList = []
    aracbilgiler = db.getInfoWithMarkaAndSeriAndYilAndModel(marka , seri, paket, yil)
    df = pd.DataFrame(aracbilgiler)
    df.rename(columns={0: 'marka', 1: 'seri', 2: 'paket', 3: 'yil', 4: 'vites', 5: 'yakit', 6: 'kasa', 7: 'motorHacim', 8: 'motorGucu'}, inplace=True)
    liste.append(df["vites"].unique().tolist())
    liste.append(df["yakit"].unique().tolist())
    liste.append(df["kasa"].unique().tolist())
    
    df["motorHacim"] = df["motorHacim"].str.replace(".", "")
    df["motorGucu"] = df["motorGucu"].str.replace(".", "")
    df["motorHacim"] = df["motorHacim"].str.replace(",", "")
    df["motorGucu"] = df["motorGucu"].str.replace(",", "")
    df["motorHacim"] = df["motorHacim"].str.replace("cm3", "")
    df["motorHacim"] = df["motorHacim"].str.replace("cc", "")
    df["motorGucu"] = df["motorGucu"].str.replace("hp", "")

    for i in df["motorHacim"].unique():
        if str(i).find("-") < 0 and str(i).find("kadar") < 0 and str(i).find("üzeri") < 0 and i != None:
            motorHacimList.append(i)
    for i in df["motorGucu"].unique():
        if str(i).find("-") < 0 and str(i).find("kadar") < 0 and str(i).find("üzeri") < 0 and i != None:
            motorGucuList.append(i)

    liste.append(motorHacimList)
    liste.append(motorGucuList)
    return liste

