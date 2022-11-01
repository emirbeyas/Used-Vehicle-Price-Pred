from pydoc import describe
from flask import Flask, redirect, render_template, request, url_for
import aracBilgisi as AB
from DbContext import getEncodedData, getEncodedIlanlar, getEncodedDataWithLeId, getCountOfMarka
import xgboost as xgb
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split, GridSearchCV,cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import pandas as pd
from flask import json
from werkzeug.exceptions import HTTPException
import pickle


app = Flask(__name__)
app.config['DEBUG'] = False

@app.route("/")
def home():
    return render_template('main.html')

@app.route("/seri", methods = ["GET", "POST"])
def seri():
    if request.method == "POST":
        marka = request.form.get("marka")
        rows = AB.seriListele(marka)
        return render_template('seri.html',  marka= marka, rows= rows)
    else:
        return redirect(url_for("home"))

@app.route("/yil", methods = ["GET", "POST"])
def yil():
    if request.method == "POST":
        rows = []
        marka = request.form.get("marka")
        seri = request.form.get("seri")
        yillar = AB.yilListele(marka, seri)
        ilkYil = int(yillar[0])
        sonYil = int(yillar[-1])
        for i in range(sonYil - ilkYil):
            rows.append(ilkYil + i)
        return render_template('yil.html',  marka= marka, seri = seri, rows= rows)
    else:
        return redirect(url_for("home"))
        

@app.route("/paket", methods = ["GET", "POST"])
def paket():
    if request.method == "POST":
        marka = request.form.get("marka")
        seri = request.form.get("seri")
        yil = request.form.get("yil")
        rows = AB.paketListele(marka, seri, yil)
        return render_template('paket.html',  marka= marka, seri = seri, yil = yil, rows= rows)
    else:
        return redirect(url_for("home"))

@app.route("/aracbilgi", methods = ["GET", "POST"])
def aracbilgi():
    if request.method == "POST":
        marka = request.form.get("marka")
        seri = request.form.get("seri")
        yil = request.form.get("yil")
        paket = request.form.get("paket")
        rows = AB.aracBilgiListele(marka, seri, yil, paket)
        return render_template('aracBilgi.html',  marka= marka, seri = seri, yil = yil, paket = paket, rows= rows)
    else:
        return redirect(url_for("home"))

@app.route("/sonuc", methods = ["GET", "POST"])
def sonuc():
    if request.method == "POST":
        marka = request.form.get("marka")
        seri = request.form.get("seri")
        paket = request.form.get("paket")
        yil = request.form.get("yil")
        km = request.form.get("km")
        vites = request.form.get("vites")
        yakit = request.form.get("yakit")
        kasa = request.form.get("kasa")
        motorHacim = request.form.get("motorHacim")
        motorGucu = request.form.get("motorGucu")
        toplamTramer = request.form.get("toplamTramer")
        sagArkaCamurluk = request.form.get("sagArkaCamurlukTxt")
        bagajKaput = request.form.get("bagajKaputTxt")
        solArkaCamurluk = request.form.get("solArkaCamurlukTxt")
        sagArkaKapi = request.form.get("sagArkaKapiTxt")
        sagOnKapi = request.form.get("sagOnKapiTxt")
        tavan = request.form.get("tavanTxt")
        solArkaKapi = request.form.get("solArkaKapiTxt")
        solOnKapi = request.form.get("solOnKapiTxt")
        sagOnCamurluk = request.form.get("sagOnCamurlukTxt")
        motorKaput = request.form.get("motorKaputTxt")
        solOnCamurluk = request.form.get("solOnCamurlukTxt")
        onTampon = request.form.get("onTamponTxt")
        arkaTampon = request.form.get("arkaTamponTxt")
        agirHasar = request.form.get("agirHasar")
        

        if int(getCountOfMarka(int(getEncodedData(marka,1))))  < 20  :
            return redirect(url_for("hesaplanamadi"))

        if km == "" or km == 0 or km == " " or int(km) < 20000 or motorGucu == None or motorHacim == None:
            return redirect(url_for("hesaplanamadi"))
        else:
            km = float(km)

        if toplamTramer == "" or toplamTramer == 0 or toplamTramer == " ":
            toplamTramer = 0
        else:
            toplamTramer = float(toplamTramer)

        df = column = {'marka':[int(getEncodedData(marka,1))],
        'seri':[int(getEncodedData(seri, 3))],
        'model':[int(getEncodedData(paket, 2))],
        'yil':[int(yil)],
        'km':[km],
        'vites':[int(getEncodedData(vites, 6))],
        'yakit':[int(getEncodedData(yakit, 5))],
        'kasa':[int(getEncodedData(kasa, 4))],
        'motorHacim':[float(motorHacim)],
        'motorGucu':[float(motorGucu)],
        'toplamTramer':[toplamTramer],
        'sagArkaCamurluk':[int(sagArkaCamurluk)],
        'arkaKaput':[int(bagajKaput)],
        'solArkaCamurluk':[int(solArkaCamurluk)],
        'sagArkaKapi':[int(sagArkaKapi)],
        'sagOnKapi':[int(sagOnKapi)],
        'tavan':[int(tavan)],
        'solArkaKapi':[int(solArkaKapi)],
        'solOnKapi':[int(solOnKapi)],
        'sagOnCamurluk':[int(sagOnCamurluk)],
        'motorKaputu':[int(motorKaput)],
        'solOnCamurluk':[int(solOnCamurluk)],
        'onTampon':[int(onTampon)],
        'arkaTampon':[int(arkaTampon)],
        'agirhasar':[int(agirHasar)]}

        model_xgb = xgb.XGBRegressor()
        model_xgb.load_model("aracimnekadarcom\model.json")
        df2 = pd.DataFrame(df)
        
        pred = model_xgb.predict(df2)
        
        
        logourl = "images/carLogos/" + marka.lower() + ".png"

        rows = []
        rows.append( getEncodedDataWithLeId(seri, 3) )
        rows.append( getEncodedDataWithLeId(paket, 2) )
        rows.append( yil )
        rows.append( motorHacim )
        rows.append( motorGucu )
        rows.append( getEncodedDataWithLeId(vites, 6) )
        rows.append( getEncodedDataWithLeId(yakit, 5) )
        rows.append( getEncodedDataWithLeId(kasa, 4) )
        rows.append( km )
        rows.append( toplamTramer )
        rows.append( logourl )
        


        return render_template('sonuc.html', tahmin = str(pred[0]).split(".")[0], rows = rows)
    else:
        return redirect(url_for("home"))
        
    
@app.errorhandler(HTTPException)
def handle_exception(e):
    return render_template('error.html', code = e.code, name = e.name, description = e.description)


@app.route("/hesaplanamadi")
def hesaplanamadi():
    return render_template('hesaplanamadi.html')

if __name__ == "__main__":
    app.run()