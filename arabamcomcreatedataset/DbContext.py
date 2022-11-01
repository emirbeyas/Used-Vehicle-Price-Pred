from asyncio.windows_events import NULL
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

def addAdvert(ilanNo, marka, seri, model, yil, km, vites, yakit, kasa, motorHacim, motorGucu, aciklama, toplamTramer, Fiyat, sagArkaCamurluk, arkaKaput, solArkaCamurluk, sagArkaKapi, sagOnKapi, tavan, solArkaKapi, solOnKapi, sagOnCamurluk, motorKaputu, solOnCamurluk, onTampon, arkaTampon, agirhasar):
    try:
        cmd = "INSERT INTO Tbl_Ilanlar (ilanNo, marka, seri, model, yil, kilometre, vites, yakit, kasa, motorHacim, motorGucu, aciklama, toplamTramer, Fiyat, agirHasar) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        veriler = (ilanNo, marka, degiskenKontrol(seri), degiskenKontrol(model), yil, km, vites, yakit, kasa, degiskenKontrol(motorHacim), degiskenKontrol(motorGucu), degiskenKontrol(aciklama), toplamTramer, Fiyat, agirhasar)
        imlec.execute(cmd, veriler)
        db.commit()
        
        cmd = "UPDATE Tbl_Ilanlar SET sagArkaCamurluk = ?, arkaKaput = ?, solArkaCamurluk = ?, sagArkaKapi = ?, sagOnKapi = ?, tavan = ?, solArkaKapi = ?, solOnKapi = ?, sagOnCamurluk = ?, motorKaputu = ?, solOnCamurluk = ?, onTampon = ?, arkaTampon = ? WHERE ilanNo = ?"
        veriler = (sagArkaCamurluk, arkaKaput, solArkaCamurluk, sagArkaKapi, sagOnKapi, tavan, solArkaKapi, solOnKapi, sagOnCamurluk, motorKaputu, solOnCamurluk, onTampon, arkaTampon, ilanNo)
        imlec.execute(cmd, veriler) 
        db.commit()
    except:
        print("ilan veritabanında zaten bulunuyor olabilir.")

def getAdvertList():
    cmd = "SELECT * FROM Tbl_Ilanlar"
    imlec.execute(cmd)
    ilanlar = imlec.fetchall()
    return ilanlar

def getAdvertWhereList(whereCmd):
    cmd = "SELECT * FROM Tbl_Ilanlar WHERE " + whereCmd
    imlec.execute(cmd)
    ilanlar = imlec.fetchall()
    return ilanlar

def addIlanLink(ilanLink):
    try:
        cmd = "INSERT INTO Tbl_IlanLinkler VALUES (?, ?)"
        veriler = (ilanLink, datetime.datetime.today())
        imlec.execute(cmd, veriler)
        db.commit()
    except:
        print("veritabanında var amk")

def getIlanLink():
    try:
        cmd = "SELECT ilanLink FROM Tbl_IlanLinkler"
        imlec.execute(cmd)
        ilanLinkler = imlec.fetchall()
        return ilanLinkler
    except:
        print("ilan veritabanında zaten bulunuyor")
