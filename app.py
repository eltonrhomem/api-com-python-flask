from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'JRR Tolkien'
    },
    {
        'id': 2,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'JK Howling'
    },
    {
        'id': 3,
        'titulo': 'James Clear',
        'autor': 'Hábitos Atômicos'
    },
]

# Consultar (todos)


@app.route('/livros', methods=['GET'])
def obterLivros():
    return jsonify(livros)

# Consultar por id


@app.route('/livros/<int:id>', methods=['GET'])
def obterLivro(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)


# Editar livro por ID
@app.route('/livros/<int:id>', methods=['PUT'])
def editarLivro(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# Incluir novo livro


@app.route('/livros', methods=['POST'])
def criarLivro():
    novoLivro = request.get_json()
    livros.append(novoLivro)
    return jsonify(novoLivro)

# Excluir livro


@app.route('/livros/<int:id>', methods=['DELETE'])
def excluirLivro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)
