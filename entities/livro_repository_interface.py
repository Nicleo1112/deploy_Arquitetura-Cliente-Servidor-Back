from abc import ABC, abstractmethod

class LivroRepositoryInterface(ABC):

    @abstractmethod
    def listar_todos(self):
        pass

    @abstractmethod
    def adicionar(self, livro):
        pass

    @abstractmethod
    def remover(self, titulo):
        pass
