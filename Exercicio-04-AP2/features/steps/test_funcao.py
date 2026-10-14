import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from behave import given, then, when
from calculadora import soma


@given("primeiro valor será {valor:d}")
def step_primeiro_valor(context, valor):
    context.primeiro = valor


@given("segundo valor será {valor:d}")
def step_segundo_valor(context, valor):
    context.segundo = valor


@when("executa a função")
def step_executa_funcao(context):
    context.resultado = soma(context.primeiro, context.segundo)


@then("saida deverá ser o valor {esperado:d}")
def step_saida(context, esperado):
    assert context.resultado == esperado, (
        f"Esperado {esperado}, mas veio {context.resultado}"
    )
