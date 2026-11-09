import pytest
from playwright.sync_api import Page, expect
from axe_playwright_python.sync_playwright import Axe
from pages.classificador_page import ClassificadorPage

@pytest.mark.e2e
def test_fluxo_completo_classificacao(page: Page, server_url: str):
    page.goto(server_url)
    pagina = ClassificadorPage(page)
    
    pagina.preencher_formulario("9.0", "8.0", "8.5", "18")
    pagina.calcular()
    
    expect(pagina.resultado).to_contain_text("Acesso Liberado")
    expect(pagina.resultado).to_contain_text("Pode assistir")

@pytest.mark.accessibility
def test_acessibilidade_wcag(page: Page, server_url: str):
    page.goto(server_url)
    axe = Axe()
    results = axe.run(page)
    violations = results.response.get("violations", [])
    assert len(violations) == 0, f"Erros de acessibilidade: {violations}"

@pytest.mark.accessibility
def test_navegacao_por_teclado(page: Page, server_url: str):
    page.goto(server_url)
    page.keyboard.press("Tab")
    expect(page.get_by_label("Nota 1")).to_be_focused()