from datetime import date
from tests.produtoRepositorioFake import ProdutoRepositorioFake
from src.produto import Produto
from src.produtoServico import ProdutoServico

def test_inserir_um_produto_deve_retornar_valor_20():
     produtoRepositorio = ProdutoRepositorioFake()
     produtoServico = ProdutoServico(produtoRepositorio)
     produto1 = Produto('1', 'Arroz 1kg', 20.0) 
     
     produtoServico.insere_produto(produto1)
     
     assert produtoServico.obter_valor() == 20


def test_buscar_todos_deve_retornar_lista_com_produtos_inseridos():
    produtoRepositorio = ProdutoRepositorioFake()
    produtoServico = ProdutoServico(produtoRepositorio)
    produto1 = Produto('1', 'Arroz 1kg', 20.0)
    produto2 = Produto('2', 'Feijão 1kg', 10.0)

    produtoServico.insere_produto(produto1)
    produtoServico.insere_produto(produto2)

    resultado = produtoRepositorio.buscar_todos()

    assert len(resultado) == 2
    assert resultado[0].titulo == 'Arroz 1kg'
    assert resultado[1].titulo == 'Feijão 1kg'

def test_repositorio_vazio_deve_retornar_valor_zero():
    produtoRepositorio = ProdutoRepositorioFake()
    produtoServico = ProdutoServico(produtoRepositorio)

    assert produtoServico.obter_valor() == 0.0