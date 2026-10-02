from flask import Flask, render_template, request

app = Flask(__name__, template_folder=".", static_folder="assets", static_url_path="/assets")

# Variáveis globais simples para guardar as quantidades e valores de venda
qtd_ovo = 16
qtd_leite = 10
qtd_queijo = 8

preco_ovo = 5.00
preco_leite = 4.00
preco_queijo = 35.00

# Variáveis para guardar o custo com valores iniciais padrão
custo_ovo = "0.00"
custo_leite = "0.00"
custo_queijo = "0.00"
custo_total = "0.00"

@app.route("/")
def ola():
    return render_template(
        "index.html", 
        qtd_ovo=qtd_ovo, qtd_leite=qtd_leite, qtd_queijo=qtd_queijo,
        preco_ovo=preco_ovo, preco_leite=preco_leite, preco_queijo=preco_queijo
    )

@app.route("/carrinho")
def carrinho():
    return render_template("carrinho.html")

@app.route("/admin", methods=["GET", "POST"])
def admin():
    global qtd_ovo, qtd_leite, qtd_queijo
    global preco_ovo, preco_leite, preco_queijo
    global custo_ovo, custo_leite, custo_queijo, custo_total

    if request.method == "POST":
        # 1. Pega os valores que o administrador digitou
        qtd_ovo = int(request.form.get("duziaovos", 0))
        qtd_leite = float(request.form.get("litrosdeleite", 0))
        qtd_queijo = float(request.form.get("kilodequeijo", 0))

        preco_ovo = float(request.form.get("valorovo", 5.00))
        preco_leite = float(request.form.get("valorleite", 4.00))
        preco_queijo = float(request.form.get("valorqueijo", 35.00))

        digovo = float(request.form.get("digovo", 0))
        digoleite = float(request.form.get("digoleite", 0))
        digoqueijo = float(request.form.get("digoqueijo", 0))

        # 2. Faz os cálculos matemáticos e formata como texto (duas casas decimais)
        calc_ovo = qtd_ovo * digovo
        calc_leite = qtd_leite * digoleite
        calc_queijo = qtd_queijo * digoqueijo
        calc_total = calc_ovo + calc_leite + calc_queijo

        custo_ovo = f"{calc_ovo:.2f}"
        custo_leite = f"{calc_leite:.2f}"
        custo_queijo = f"{calc_queijo:.2f}"
        custo_total = f"{calc_total:.2f}"

    return render_template(
        "admin.html", 
        qtd_ovo=qtd_ovo, qtd_leite=qtd_leite, qtd_queijo=qtd_queijo,
        preco_ovo=preco_ovo, preco_leite=preco_leite, preco_queijo=preco_queijo,
        custo_ovo=custo_ovo, custo_leite=custo_leite, 
        custo_queijo=custo_queijo, custo_total=custo_total
    )

if __name__ == "__main__":
    app.run(debug=True)
