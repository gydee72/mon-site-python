from flask import Flask, render_template, request, Response
from functools import wraps
from database import init_db, ajouter_message, get_messages

app = Flask(__name__)
init_db()

# Identifiants (à changer !)
ADMIN_USER = "gydee"
ADMIN_PASSWORD = "Rbk7172*"

def verifier_auth(username, password):
    return username == ADMIN_USER and password == ADMIN_PASSWORD

def authentification_requise():
    return Response(
        "Accès refusé. Merci de vous identifier.", 401,
        {"WWW-Authenticate": 'Basic realm="Login requis"'}
    )

def login_requis(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not verifier_auth(auth.username, auth.password):
            return authentification_requise()
        return f(*args, **kwargs)
    return decorated


@app.route("/")
def accueil():
    return render_template("accueil.html", nom="Visiteur")

@app.route("/apropos")
def apropos():
    return render_template("apropos.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        nom = request.form.get("nom")
        email = request.form.get("email")
        message = request.form.get("message")

        ajouter_message(nom, email, message)

        return render_template("contact.html", message_envoye=True, nom=nom)

    return render_template("contact.html")

@app.route("/messages")
@login_requis
def messages():
    tous_les_messages = get_messages()
    return render_template("messages.html", messages=tous_les_messages)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)