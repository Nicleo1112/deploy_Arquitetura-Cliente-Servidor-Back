import os
from entities.livro import Livro
from entities.livro_repository_interface import LivroRepositoryInterface

ARQUIVO = os.path.join(os.path.dirname(os.path.dirname(__file__)), "livros.txt")

LIVROS_INICIAIS = [
    "Harry Potter e a Pedra Filosofal|J.K Rowling|1997",
    "Harry Potter e a Câmara Secreta|J.K Rowling|1998",
    "O Hobbit|Tolkien|1937",
    "O Senhor dos Anéis|Tolkien|1954",
    "Dom Casmurro|Machado de Assis|1899",
    "Memórias Póstumas de Brás Cubas|Machado de Assis|1881",
    "Clean Code|Robert C. Martin|2008",
    "Clean Architecture|Robert C. Martin|2017",
    "Python Crash Course|Eric Matthes|2015",
    "Automate the Boring Stuff|Al Sweigart|2015",
    "The Pragmatic Programmer|Andrew Hunt|1999",
    "Design Patterns|Erich Gamma|1994",
    "Refactoring|Martin Fowler|1999",
    "Código Limpo|Robert C. Martin|2009",
    "Algoritmos|Thomas H. Cormen|2009",
    "Estruturas de Dados|Narasimha Karumanchi|2011",
    "Redes de Computadores|Andrew S. Tanenbaum|2010",
    "Sistemas Operacionais|Andrew S. Tanenbaum|2015",
    "Engenharia de Software|Ian Sommerville|2011",
    "Introdução à Programação|Deitel|2012",
    "Java: Como Programar|Deitel|2016",
    "C Programming Language|Kernighan|1988",
    "Artificial Intelligence|Stuart Russell|2010",
    "Deep Learning|Ian Goodfellow|2016",
    "Banco de Dados|Elmasri|2015",
    "Compiladores|Aho|2006",
    "Computer Organization|Patterson|2013",
    "Digital Design|Morris Mano|2012",
    "Data Science Handbook|Jake VanderPlas|2016",
    "Fluent Python|Luciano Ramalho|2015",
]

class TxtLivroRepository(LivroRepositoryInterface):

    def __init__(self):
        self._inicializar_arquivo()

    def _inicializar_arquivo(self):
        if not os.path.exists(ARQUIVO) or os.path.getsize(ARQUIVO) == 0:
            with open(ARQUIVO, "w", encoding="utf-8") as f:
                f.write("\n".join(LIVROS_INICIAIS) + "\n")

    def listar_todos(self):
        livros = []
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    partes = linha.split("|")
                    if len(partes) == 3:
                        livros.append(Livro(partes[0], partes[1], partes[2]))
        return livros

    def adicionar(self, livro):
        with open(ARQUIVO, "a", encoding="utf-8") as f:
            f.write(f"{livro.titulo}|{livro.autor}|{livro.ano}\n")

    def remover(self, titulo):
        livros = self.listar_todos()
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            for livro in livros:
                if livro.titulo.lower() != titulo.lower():
                    f.write(f"{livro.titulo}|{livro.autor}|{livro.ano}\n")
