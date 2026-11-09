from playwright.sync_api import Page, Locator

class ClassificadorPage:
    def __init__(self, page: Page):
        self.page = page
        self.input_n1: Locator = page.get_by_label("Nota 1")
        self.input_n2: Locator = page.get_by_label("Nota 2")
        self.input_n3: Locator = page.get_by_label("Nota 3")
        self.input_idade: Locator = page.get_by_label("Idade")
        self.btn_calcular: Locator = page.get_by_role("button", name="Calcular Classificação")
        self.resultado: Locator = page.get_by_role("status")

    def preencher_formulario(self, n1: str, n2: str, n3: str, idade: str):
        self.input_n1.fill(n1)
        self.input_n2.fill(n2)
        self.input_n3.fill(n3)
        self.input_idade.fill(idade)

    def calcular(self):
        self.btn_calcular.click()