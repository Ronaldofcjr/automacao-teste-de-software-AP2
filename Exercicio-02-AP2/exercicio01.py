from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path

# Cria o navegador
driver = webdriver.Chrome()

# Obtém o caminho absoluto do arquivo HTML
arquivo = Path("exercicio01.html").resolve()

# Abre o arquivo local
driver.get(arquivo.as_uri())

# a) Mostra o título da página
print("Título da página:", driver.title)

# b) Localiza o parágrafo utilizando TAG_NAME
paragrafo_tag = driver.find_element(By.TAG_NAME, "p")
print("Conteúdo usando TAG_NAME:", paragrafo_tag.text)

# c) Localiza o parágrafo utilizando CSS_SELECTOR
paragrafo_css = driver.find_element(By.CSS_SELECTOR, "p.content")
print("Conteúdo usando CSS_SELECTOR:", paragrafo_css.text)

# Fecha o navegador
driver.quit()
