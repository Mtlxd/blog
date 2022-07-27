#pip freeze mostra a o que esta instalado no ambiente
#pip freeze > nome.txt salva as instalações do ambiente
#pip install -r requirements.txt (carrega as configurações do requeriments)
#Ferramenta de Dev no browser CTRL+SHIFT+I
from flask import Flask, render_template #bibliotecas usadas
from datetime import datetime
app = Flask('hello')

posts = [
    {
        'title': 'O meu Primeiro Post',
        'body' : 'Aqui é o texto do Post',
        'author': 'Feulo',
        'created': datetime(2022,7,25)
    },
    {
        'title': 'O meu segundo Post',
        'body' : 'Aqui é o texto do Post',
        'author': 'Danilo',
        'created': datetime(2022,7,26)
    },
]

@app.route('/') #Cria uma rota para a aplicação (raiz da aplicação)
#Route permite que a gente atribua uma função
#o '@'é uma anotação para rota
def index():
    return render_template('index.html', posts=posts) #flask run (para rodar)
