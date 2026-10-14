from src.produto import Produto
from src.produtoRepositorio import ProdutoRepositorio

class ProdutoRepositorioFake(ProdutoRepositorio):
    def __init__(self):
        self.produtos = []

    def inserir(self, produto: Produto):
        self.produtos.append(produto)

    def buscar_todos(self) -> list:
        return list(self.produtos)

    def obter_valor(self) -> float:
        return sum(p.valor for p in self.produtos)