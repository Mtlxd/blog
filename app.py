#pip freeze mostra a o que esta instalado no ambiente
#pip freeze > nome.txt salva as instalações do ambiente
#pip install -r requirements.txt (carrega as configurações do requeriments)
#Ferramenta de Dev no browser CTRL+SHIFT+I
from flask import Flask, render_template #bibliotecas usadas

app = Flask('hello')

@app.route('/') #Cria uma rota para a aplicação (raiz da aplicação)
#Route permite que a gente atribua uma função
#o '@'é uma anotação para rota
@app.route('/hello')#Rota do servidor
def hello():
    return 'Hello World!' #flask run (para rodar)

@app.route('/meucontato')#Rota do servidor
def meuContato():
    return render_template('index.html')
    