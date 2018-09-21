import sys
sys.path.append("/storage/emulated/0/programming/appPharma")

from appPharma.calculPharma import bmi, aw

from flask import Flask, render_template, request
app = Flask(__name__)


# cd /storage/emulated/0/programming/appPharma/web && python main.py

app.jinja_env.globals.update(zip=zip)

PAGE = ["Indice de masse corporelle", 
                      "Poids ajusté", 
                      "Poids Ideal", 
                      "clairance a la creatinine"]
URL = list(map(lambda page: page.replace(" ", "_"), PAGE))

@app.route('/')
def accueil():
    return render_template('accueil.html', titre="Application de calcul pharmaceutique", navigation=PAGE, urls=URL)

@app.route(f'/{URL[0]}', methods=['GET', 'POST'])
def Indice_de_masse_corporelle():
    if request.method == 'POST':
        taille = request.form['taille']
        poids = request.form['poids']
        imc = f"{bmi(poids, taille):.2f~P}"
        return render_template('IMC.html', titre=PAGE[0], result = imc, taille=taille, poids=poids)
    return render_template('IMC.html', titre=PAGE[0])

@app.route(f'/{URL[1]}', methods=['GET', 'POST'])
def Poids_ajusté():
    if request.method == 'POST':
        taille = request.form['taille']
        poids = request.form['poids']
        femme = True if request.form.get('femme', False) == "on" else False
        checked = "checked" if femme else None
        pa = f"{aw(poids, taille, F=femme):.2f~P}"
        return render_template('pa.html', titre=PAGE[1], result = pa, taille=taille, poids=poids, checked=checked)
    return render_template('PA.html', titre=PAGE[1])

@app.route(f'/{URL[2]}')
def Poids_Ideal():
    return render_template('base_calcul.html', titre=PAGE[2])

@app.route(f'/{URL[3]}')
def clairance_a_la_creatinine():
    return render_template('base_calcul.html', titre=PAGE[3])

if __name__ == '__main__':
    app.run(debug=True)