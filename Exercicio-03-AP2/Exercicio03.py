import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

PAUSA = 0.8

driver = webdriver.Chrome()
driver.maximize_window()

# Abre o HTML local (funciona de qualquer pasta)
arquivo = Path(__file__).parent / "exercicio03.html"
driver.get(arquivo.resolve().as_uri())
print("Título da página:", driver.title)
time.sleep(PAUSA)

# Nome - ID
driver.find_element(By.ID, "nome").send_keys("Ronaldo Filgueira Cavalcante")
time.sleep(PAUSA)

# RA - NAME
driver.find_element(By.NAME, "ra").send_keys("2403661")
time.sleep(PAUSA)

# Data de nascimento - dia (ID), mês (CSS_SELECTOR), ano (XPATH)
Select(driver.find_element(By.ID, "dia")).select_by_value("20")
time.sleep(PAUSA)

Select(driver.find_element(By.CSS_SELECTOR, "select#mes")).select_by_value("7")
time.sleep(PAUSA)

Select(driver.find_element(By.XPATH, "//select[@name='ano']")).select_by_value("1994")
time.sleep(PAUSA)

# Curso - ID
Select(driver.find_element(By.ID, "curso")).select_by_visible_text(
    "Análise e desenvolvimento de Sistemas"
)
time.sleep(PAUSA)

# Aproveitamento do conteúdo - NAME
Select(driver.find_element(By.NAME, "aproveitamento")).select_by_value("9")
time.sleep(PAUSA)

# Sugestões - CSS_SELECTOR
driver.find_element(By.CSS_SELECTOR, "textarea#sugestoes").send_keys(
    "Mais exercícios práticos com Selenium e testes em projetos reais."
)
time.sleep(PAUSA)

# Observações (opcional) - XPATH
driver.find_element(By.XPATH, "//textarea[@id='observacoes']").send_keys(
    "Gostei muito da disciplina."
)
time.sleep(PAUSA)

# Print do formulário preenchido (antes de enviar)
driver.save_screenshot(str(Path(__file__).parent / "print_formulario.png"))
time.sleep(PAUSA)

# Enviar Feedback - CLASS_NAME
driver.find_element(By.CLASS_NAME, "botao-enviar").click()
time.sleep(PAUSA)

mensagem = driver.find_element(By.ID, "mensagem")
print("Mensagem na tela:", mensagem.text)

# Print após o envio
driver.save_screenshot(str(Path(__file__).parent / "print_apos_envio.png"))
time.sleep(PAUSA)

driver.quit()