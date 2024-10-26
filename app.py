from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Função para gerar números aleatórios e a resposta correta
def gerar_pergunta():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return num1, num2, num1 * num2

@app.route('/', methods=['GET', 'POST'])
def index():
    # Inicializa variáveis
    mensagem = None

    if request.method == 'POST':
        try:
            # Coleta a resposta do usuário e tenta converter para inteiro
            resposta_usuario = int(request.form.get('resposta'))
            num1 = int(request.form.get('num1'))
            num2 = int(request.form.get('num2'))
            resposta_correta = int(request.form.get('resposta_correta'))

            # Verifica se a resposta está correta
            if resposta_usuario == resposta_correta:
                mensagem = "Resposta correta! Parabéns!"
                # Gera uma nova pergunta
                num1, num2, resposta_correta = gerar_pergunta()
            else:
                mensagem = "Resposta errada, tente de novo."
        except ValueError:
            # Caso a conversão falhe (se o usuário não digitar um número), exibe um erro
            mensagem = "Entrada inválida! Por favor, insira apenas números."

    else:
        # Se for GET, gera uma nova pergunta
        num1, num2, resposta_correta = gerar_pergunta()

    return render_template('perguntas.html', num1=num1, num2=num2, mensagem=mensagem, resposta_correta=resposta_correta)

if __name__ == '__main__':
    app.run(debug=True)
