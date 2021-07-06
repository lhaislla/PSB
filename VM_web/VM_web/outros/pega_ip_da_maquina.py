from flask import Flask,jsonify,render_template
from requests import get
# Bibliotecas Ip e CPU:
import socket
import psutil


#from app import app


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["GET", "POST"])
# Endereço da Máquina:
@app.route("/info", methods=["GET", "POST"])
def info():
    hostname = socket.gethostname()
    ip_interno = socket.gethostbyname(hostname)
    ip_externo = get('https://api.ipify.org').text
    cpu = psutil.cpu_percent()
    total_memoria = psutil.virtual_memory()
    resultado = (f"<br>Hostname:{hostname}",
                 f" IP Interno: {ip_interno}",
                 f" IP Interno: {ip_interno}",
                 f" IP Externo: {ip_externo}",
                 f" Memoria CPU: {cpu}",
                 f"Informacoes da Memoria: {total_memoria}")
    opcao = ''
    saida = ''
    while opcao != '1' or '2':
        opcao = input("""Selecione o sistema que deseja as informaçoes: \n
        1 - Windows \n
        2 - Linux\n """)

        if opcao == '1':
            saida = f" <br><ol>Informações Windows: {resultado}</br>"
            return(saida)
        elif opcao == '2':
            saida = f" <br> Informações Linux:\n {resultado}</br>"
            return(saida)
    #print('<h1>Informação PC</h1>')
    return jsonify(saida)


#print(info())
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, debug=True)
