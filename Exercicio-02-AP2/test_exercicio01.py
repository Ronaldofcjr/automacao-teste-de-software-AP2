import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


class TestExercicio01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

        arquivo = os.path.abspath("exercicio01.html")
        cls.driver.get("file://" + arquivo)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_titulo(self):
        self.assertEqual(
            self.driver.title,
            "Exercício 01"
        )

    def test_paragrafo_tag_name(self):
        paragrafo = self.driver.find_element(By.TAG_NAME, "p")

        self.assertEqual(
            paragrafo.text,
            "O conteúdo do site vem aqui"
        )

    def test_paragrafo_css_selector(self):
        paragrafo = self.driver.find_element(
            By.CSS_SELECTOR,
            "p.content"
        )

        self.assertEqual(
            paragrafo.text,
            "O conteúdo do site vem aqui"
        )


if __name__ == "__main__":
    unittest.main()
