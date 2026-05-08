from entities.livro import Livro

class LivroUseCases:
    def __init__(self, repository):
        self.repository = repository

    def filtrar(self, titulo="", autor="", ano_inicio=None, ano_fim=None):
        livros = self.repository.listar_todos()
        resultado = []
        for livro in livros:
            if titulo and titulo.lower() not in livro.titulo.lower():
                continue
            if autor and autor.lower() not in livro.autor.lower():
                continue
            if ano_inicio is not None and ano_fim is not None:
                if livro.ano < ano_inicio or livro.ano > ano_fim:
                    continue
            resultado.append(livro)
        return resultado

    def adicionar(self, titulo, autor, ano):
        if not titulo or not autor or not ano:
            raise ValueError("Todos os campos são obrigatórios.")
        if int(ano) < 0 or int(ano) > 2100:
            raise ValueError("Ano inválido.")
        livro = Livro(titulo, autor, int(ano))
        self.repository.adicionar(livro)

    def remover(self, titulo):
        if not titulo:
            raise ValueError("Título obrigatório para remover.")
        self.repository.remover(titulo)
