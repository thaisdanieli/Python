# API - É um lugar para disponibilizar recursos e/ou funcionalidades

# 1. Objetivo  - Criar uma API que disponibiliza a consulta, criação, edição e exclusão de livros.
# 2. URL base  - localhost
# 3. Endpoints - 
#               - localhost/livros (GET)        *Consultar*
#               - localhost/livros/id (GET)     *Obter algo pelo id (Pesquisa)* 
#               - localhost/livros/id (POST)    *Criar Novos Livros*
#               - localhost/livros/id (PUT)     *Modificar*
#               - localhost/livros/id (DELETE)  
# 4. Quais recursos - Livros


# Request permite acessar os dados que estão indo e vindo nas requisições
# Aqui, o código importa as classes Flask (para criar o servidor), jsonify (para converter objetos Python em JSON) e request (para acessar dados das requisições HTTP).
from flask import Flask, jsonify, request

# Servidor que estará hospedando está API
# Cria uma instância da classe Flask para o aplicativo.

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
# Define uma rota /livros para obter todos os livros quando uma requisição GET é feita.


@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar (Id)
# Define uma rota /livros/<int:id> para obter um livro específico pelo ID quando uma requisição GET é feita.

@app.route('/livros/<int:id>', methods=['GET'])
def livro_Id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# Editar
# Define uma rota /livros/<int:id> para editar um livro específico pelo ID quando uma requisição PUT é feita.

@app.route('/livros/<int:id>', methods=['PUT'])
def editarLivro_ID(id):
    livroAlterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livroAlterado)
            return jsonify(livros[indice])

# Criar
# Define uma rota /livros para adicionar um novo livro quando uma requisição POST é feita.

@app.route('/livros', methods=['POST'])
def incluirNovo_Livro():
    novo_Livro = request.get_json()
    livros.append(novo_Livro)

    return jsonify(livros)

# Excluir
# Define uma rota /livros/<int:id> para excluir um livro específico pelo ID quando uma requisição DELETE é feita.

@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_Livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    
    return jsonify(livros)

# Inicia o servidor Flask na porta 5000, com o host definido como 'localhost' e com modo de depuração ativado. O modo de depuração permite visualizar mensagens de erro detalhadas durante o desenvolvimento.

app.run(port=5000, host='localhost', debug=True)



