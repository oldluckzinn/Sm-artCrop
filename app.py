from flask import Flask, render_template
from data import verduras

app = Flask(__name__)

@app.route('/')
def  home():
    return render_template('index.html')

@app.route('/data/<nome>')
def mostrar_verdura(nome):
    verdura_info = verduras.get(nome)
    if verdura_info:
        return render_template('data.html', dados=verdura_info)
    else:
        return "Verdura não encontrada", 404
    
if __name__ == '__main__':
    app.run(debug=True)
