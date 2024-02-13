# Request permite acessar os dados que estão indo e vindo nas requisições
from flask import Flask, jsonify, request

# Servidor que estará hospedando está API

app = Flask(__name__)

# Adicionar dentro de uma lista de dicionarios
livros = [
    {
        'id': 1,
        'título': 'O Senhor dos Anéis: A Sociedade do Anel',
        'autor': 'J. R. R. Tolkien'
    },
    {
        'id': 2,
        'título': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J. K. Rowling'
    },
    {
        'id': 3,
        'título': 'James Clear',
        'autor': 'Hábitos Atômicos'
    },
]

# Consultar (Todos)


@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar (Id)


@app.route('/livros/<int:id>', methods=['GET'])
def livro_Id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# Editar


@app.route('/livros/<int:id>', methods=['PUT'])
def editarLivro_ID(id):
    livroAlterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livroAlterado)
            return jsonify(livros[indice])

# Criar


@app.route('/livros', methods=['POST'])
def incluirNovo_Livro():
    novo_Livro = request.get_json()
    livros.append(novo_Livro)

    return jsonify(livros)

# Excluir

@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_Livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    
    return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)
