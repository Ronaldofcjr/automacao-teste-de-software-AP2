from abc import ABCMeta, abstractmethod
from src.produto import Produto

class ProdutoRepositorio():

    def inserir(self, produto: Produto):
        pass

 
    def buscar_todos(self) -> list:
        pass


    def obter_valor(self) -> float:
        pass 


