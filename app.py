from flask import Flask, request, render_template, url_for
import joblib
import numpy as np

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('ingresarDatos.html')  # pagina principal


@app.route("/predecir", methods=["POST", ])
def predecir():
    inicio = int(request.form['inicio'])
    cursos = int(request.form['cursos'])
    contacto = int(request.form['contacto'])

    modelo = joblib.load('./modelo.pkl')
    # prediccion=modelo.predict([[1,0,1]])
    entrada = np.array([[inicio, cursos, contacto]])
    prediccion = modelo.predict(entrada)
    if prediccion[0] == 0:
        resultado = "No Compra"
        foto = "noComprar.jpg"
    else:
        resultado = "Compra"
        foto = "comprar.jpg"

    return render_template('resultado.html', resultado=resultado, foto=foto)  # pagina resultado


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)