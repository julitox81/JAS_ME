from flask import Flask, render_template

app = Flask(__name__, template_folder='')

# Dados fictícios para produtos
produtos = [
    {
        'nome': 'Produto 1',
        'imagem': 'produto1.jpg',
        'valor': '100.00',
        'descricao': 'Descrição do Produto 1',
        'funcionalidades': 'Funcionalidade 1, Funcionalidade 2',
        'material': 'Material do Produto 1'
    },
    {
        'nome': 'Produto 2',
        'imagem': 'produto2.jpg',
        'valor': '150.00',
        'descricao': 'Descrição do Produto 2',
        'funcionalidades': 'Funcionalidade 1, Funcionalidade 2',
        'material': 'Material do Produto 2'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/servicos')
def servicos():
    return render_template('servicos.html')

@app.route('/loja')
def loja():
    return render_template('loja.html', produtos=produtos)

@app.route('/produto/<nome_produto>')
def produto(nome_produto):
    produto = next((p for p in produtos if p['nome'] == nome_produto), None)
    if produto is None:
        return "Produto não encontrado", 404
    return render_template('produto.html', produto=produto)

@app.route('/quem_somos')
def quem_somos():
    return render_template('quem_somos.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)
