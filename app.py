from flask import Flask, render_template

app = Flask(__name__, template_folder=".", static_folder="assets", static_url_path="/assets")


@app.route("/")
def ola():
    # Em vez de retornar um texto, o Flask agora vai abrir o seu arquivo html
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
