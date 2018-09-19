from flask import Flask, render_template
app = Flask(__name__)
import appPharma.calculPharma

# cd /storage/emulated/0/programming/appPharma/appPharma/web && python main.py

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
        imc = bmi(request.form['poids'], request.form['taille'])
        return "IMC : {imc}".format(imc=imc)
    return render_template('IMC.html', titre=PAGE[0])

@app.route(f'/{URL[1]}')
def Poids_ajusté():
    return render_template('base_calcul.html', titre=PAGE[1])

@app.route(f'/{URL[2]}')
def Poids_Ideal():
    return render_template('base_calcul.html', titre=PAGE[2])

@app.route(f'/{URL[3]}')
def clairance_a_la_creatinine():
    return render_template('base_calcul.html', titre=PAGE[3])

if __name__ == '__main__':
    app.run(debug=True)