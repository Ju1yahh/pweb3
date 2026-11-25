from flask import Flask, render_template, request, redirect
import aluno_service
import curso_service

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", titulo="Minha primeira aplicação Flask")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/ola/<nome>")
def ola(nome):
    return render_template("ola.html", nome=nome)

@app.route("/idade/<int:idade>")
def idade(idade):
    return render_template("idade.html", idade=idade)

@app.route("/disciplinas")
def disciplinas():
    lista = ["Progamação Web", "Banco de Dados", "Redes", "Inglês Técnico"]
    return render_template("disciplinas.html", disciplinas=lista)

@app.route("/tabuada/<int:n>")
def tabuada(n):
    return render_template("tabuada.html", n=n)

@app.route("/aluno/")
def listar_aluno():
    alunos = aluno_service.listar()
    return render_template("aluno/listar.html", alunos=alunos)

@app.route("/aluno/novo")
def novo_aluno():
    return render_template("aluno/form.html", aluno=None)

@app.route("/aluno/salvar", methods=["POST"])
def salvar_aluno():
    id_aluno = request.form["id"]
    nome = request.form["nome"]
    telefone = request.form["telefone"]
    cidade = request.form["cidade"]

    if id_aluno == "":
        aluno_service.cadastrar(nome, telefone, cidade)
    # Próxima aula: se o id vier preenchido, editar o aluno


    return redirect("/aluno/")

@app.route("/curso/")
def listar_cursos():
    cursos = curso_service.listar()
    return render_template("curso/listar.html", cursos=cursos)


# deve ficar no final do arquivo sempre
if __name__ == "__main__":
    # host=0.0.0.0 permite o encaminhamento da porta no Codespaces.
    app.run(host="0.0.0.0", port=5000, debug=True)






































