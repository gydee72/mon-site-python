from flask import Flask

app = Flask(__name__)

@app.route("/")
def accueil():
    return "<h1>Bienvenue sur mon site depuis Codespace !</h1>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)