from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return u"Hello, Flask!"
print(home())
if __name__ == "__main__":
    app.run()