from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Variável global para armazenar o número aleatório (Aqui eu fiz o computador escolher um número)
numero_aleatorio = random.randint(1, 100)

@app.route("/", methods=["GET", "POST"]) #Aqui eu uso o método get para pegar e post para mostrar
def jogo_adivinhacao():
    mensagem = ""
    if request.method == "POST":
        tentativa = int(request.form["tentativa"])
        if tentativa < numero_aleatorio:
            mensagem = "Tente um número maior!"
        elif tentativa > numero_aleatorio:
            mensagem = "Tente um número menor!"
        else:
            mensagem = "Parabéns! Você acertou!"
            reiniciar_jogo()
    return render_template("index.html", mensagem=mensagem)

def reiniciar_jogo():
    global numero_aleatorio
    numero_aleatorio = random.randint(1, 100)  # Aqui eu  gerei um novo número aleatório

if __name__ == "__main__":
    app.run(debug=True)

