from asyncio.windows_events import NULL
import cmd
import datetime
import pypyodbc

db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-BQH67H2;'
    'Database=AracimNeKadarDB;'
    'Trusted_Connection=True;'
)
imlec = db.cursor()

def degiskenKontrol(Degisken):
    if Degisken == "" or Degisken == " " or Degisken == "-" or Degisken == "NaN" or Degisken == "nan" or Degisken == "none":
        return NULL 

def getAdvertList():
    cmd = "SELECT * FROM Tbl_Ilanlar"
    imlec.execute(cmd)
    ilanlar = imlec.fetchall()
    return ilanlar

def getInfoWithMarka(marka):
    cmd = "SELECT marka, seri, model, yil, vites, yakit, kasa FROM Tbl_Ilanlar WHERE REPLACE(marka, ' ', '') = '" + marka + "'"
    imlec.execute(cmd)
    aracbilgileri = imlec.fetchall()
    return aracbilgileri


def getInfoWithMarkaAndSeri(marka, seri):
    cmd = "SELECT marka, seri, model, yil, vites, yakit, kasa FROM Tbl_Ilanlar WHERE REPLACE(marka, ' ', '') = ? AND REPLACE(seri, ' ', '') = ?"
    values = (marka, seri)
    imlec.execute(cmd, values)
    aracbilgileri = imlec.fetchall()
    return aracbilgileri



def getInfoWithMarkaAndSeriAndYil(marka, seri, yil):
    cmd = "SELECT marka, seri, model, yil, vites, yakit, kasa FROM Tbl_Ilanlar WHERE REPLACE(marka, ' ', '') = ? AND REPLACE(seri, ' ', '') = ? AND yil = ?"
    values = (marka, seri, yil)
    imlec.execute(cmd, values)
    aracbilgileri = imlec.fetchall()
    return aracbilgileri



def getInfoWithMarkaAndSeriAndYilAndModel(marka, seri, model, yil):
    cmd = "SELECT marka, seri, model, yil, vites, yakit, kasa, motorHacim, motorGucu FROM Tbl_Ilanlar WHERE REPLACE(marka, ' ', '') = ? AND REPLACE(seri, ' ', '') = ? AND REPLACE(model, ' ', '') = ? AND yil = ?"
    values = (marka, seri, model, yil)
    imlec.execute(cmd, values)
    aracbilgileri = imlec.fetchall()
    return aracbilgileri


def getEncodedData(aciklama, kategori):
    cmd = "SELECT leId FROM tbl_encodedData WHERE kategori = ? and REPLACE(aciklama, ' ', '') = ?"
    values = (kategori, aciklama)
    imlec.execute(cmd, values)
    print(values)
    aracbilgileri = imlec.fetchone()[0]
    return aracbilgileri 

def getEncodedIlanlar():
    cmd = "SELECT * FROM tbl_encodedIlanlar"
    imlec.execute(cmd)
    ilanlar = imlec.fetchall()
    return ilanlar

def getEncodedDataWithLeId(aciklama, kategori):
    cmd = "SELECT aciklama FROM tbl_encodedData WHERE kategori = ? and REPLACE(aciklama, ' ', '') = ?"
    values = (kategori, aciklama)
    imlec.execute(cmd, values)
    print(values)
    aracbilgileri = imlec.fetchone()[0]
    return aracbilgileri 

#select count(*) from tbl_encodedIlanlar where marka = 35

def getCountOfMarka(markaId):
    cmd = "select count(*) from tbl_encodedIlanlar where marka = " + str(markaId)
    imlec.execute(cmd)
    aracbilgileri = imlec.fetchone()[0]
    return aracbilgileri 



