from flask import Flask, render_template, request

app = Flask(__name__)

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

        print(f"Nouveau message de {nom} ({email}) : {message}")

        return render_template("contact.html", message_envoye=True, nom=nom)

    return render_template("contact.html")




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)