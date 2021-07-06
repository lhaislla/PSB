#from re import S
from typing import Text
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    sistema = str(request.form.get("sistema"))
    ip = str(request.form.get("ip"))
    qm = str(request.form.get("qm"))
    cpu = str(request.form.get("CPU"))
    select = []
    if request.method == "GET":
        return render_template("index.html")
    else:
        select.append(f"\n Sistema Operacional: {sistema}")
        select.append(f"\n Endereço IP: {ip}")
        select.append(f"\n Quantidade de memória:{qm}")
        select.append(f"\n Quantidade de CPU: {cpu}")
        info = open("info.txt","w")
        info.writelines(select)
        info.close()  
    return Text(select)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, debug=True)
