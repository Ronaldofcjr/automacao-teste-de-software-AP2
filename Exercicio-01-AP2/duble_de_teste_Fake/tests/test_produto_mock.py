from src.produto import Produto
from src.produtoServico import ProdutoServico

class RepositorioMock:
    def __init__(self):
        self.inserir_chamado_com = []
        self.obter_valor_chamado = False
        self._valor = 0.0

    def inserir(self, produto: Produto):
        self.inserir_chamado_com.append(produto)

    def buscar_todos(self) -> list:
        return []

    def obter_valor(self) -> float:
        self.obter_valor_chamado = True
        return self._valor

def test_insere_produto_deve_chamar_inserir_uma_vez():
    mock = RepositorioMock()
    produtoServico = ProdutoServico(mock)
    produto = Produto('1', 'Arroz 1kg', 20.0)

    produtoServico.insere_produto(produto)

    assert len(mock.inserir_chamado_com) == 1
    assert mock.inserir_chamado_com[0].titulo == 'Arroz 1kg'

def test_obter_valor_deve_retornar_valor_configurado():
    mock = RepositorioMock()
    mock._valor = 20.0
    produtoServico = ProdutoServico(mock)

    resultado = produtoServico.obter_valor()

    assert resultado == 20.0
    assert mock.obter_valor_chamado == True

def test_inserir_dois_produtos_deve_chamar_inserir_duas_vezes():
    mock = RepositorioMock()
    produtoServico = ProdutoServico(mock)
    produto1 = Produto('1', 'Arroz 1kg', 20.0)
    produto2 = Produto('2', 'Feijão 1kg', 10.0)

    produtoServico.insere_produto(produto1)
    produtoServico.insere_produto(produto2)

    assert len(mock.inserir_chamado_com) == 2

def test_inserir_nao_deve_chamar_buscar_todos():
    mock = RepositorioMock()
    produtoServico = ProdutoServico(mock)
    produto = Produto('1', 'Leite', 5.0)

    produtoServico.insere_produto(produto)

    assert mock.obter_valor_chamado == False