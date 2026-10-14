from src.produto import Produto
from src.produtoRepositorio import ProdutoRepositorio

class ProdutoServico:
    def __init__(self, produtoRepositorio: ProdutoRepositorio):
        self.produtoRepositorio = produtoRepositorio

    def insere_produto(self, produto: Produto):
        self.produtoRepositorio.inserir(produto)

    def obter_valor(self):
        return self.produtoRepositorio.obter_valor()