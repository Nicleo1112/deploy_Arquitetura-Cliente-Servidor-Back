class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = int(ano)

    def to_dict(self):
        return {"Titulo": self.titulo, "Autor": self.autor, "Ano": self.ano}
