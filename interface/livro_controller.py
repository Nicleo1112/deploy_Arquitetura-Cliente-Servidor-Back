from flask import Blueprint, request, jsonify
from use_cases.livro_use_cases import LivroUseCases
from infra.txt_livro_repository import TxtLivroRepository

livro_bp = Blueprint('livro', __name__)
usecases = LivroUseCases(TxtLivroRepository())

@livro_bp.route('/', methods=['GET'])
def status():
    return jsonify({"status": "API Livraria online ✅"})

@livro_bp.route('/api/livros', methods=['GET'])
def listar():
    titulo = request.args.get('titulo', '')
    autor = request.args.get('autor', '')
    try:
        ano_min = int(request.args.get('ano_min'))
        ano_max = int(request.args.get('ano_max'))
    except (TypeError, ValueError):
        ano_min, ano_max = None, None

    livros = usecases.filtrar(titulo, autor, ano_min, ano_max)
    return jsonify([l.to_dict() for l in livros])

@livro_bp.route('/api/livros', methods=['POST'])
def adicionar():
    dados = request.get_json()
    try:
        usecases.adicionar(dados['titulo'], dados['autor'], dados['ano'])
        return jsonify({"mensagem": "Livro adicionado com sucesso."}), 201
    except (ValueError, KeyError) as e:
        return jsonify({"erro": str(e)}), 400

@livro_bp.route('/api/livros/<titulo>', methods=['DELETE'])
def remover(titulo):
    try:
        usecases.remover(titulo)
        return jsonify({"mensagem": "Livro removido com sucesso."}), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400
