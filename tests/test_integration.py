import pytest
from fastapi.testclient import TestClient
from app.main import app
from tests.factories import ClassificacaoFactory


@pytest.mark.integration
def test_classificar_sucesso(client):
    dados = ClassificacaoFactory.criar()
    response = client.post("/api/classificar", json=dados)

    assert response.status_code == 200
    data = response.json()
    assert "indice" in data
    assert "acesso" in data
    assert "permissao_idade" in data

@pytest.mark.integration
def test_classificar_com_mock(client, mocker):
    mocker.patch(
        "app.main.ClassificadorEva.determinar_acesso",
        return_value="Acesso Mockado"
    )
    dados = ClassificacaoFactory.criar()
    response = client.post("/api/classificar", json=dados)
    
    assert response.status_code == 200
    assert response.json()["acesso"] == "Acesso Mockado"

@pytest.mark.integration
def test_classificar_dados_invalidos(client):
    dados_invalidos = {"n1": 15.0, "n2": 5.0, "n3": 5.0, "idade": 20}
    response = client.post("/api/classificar", json=dados_invalidos)
    assert response.status_code == 422

@pytest.mark.integration
def test_classificar_com_mock_de_falha(mocker):
    client_falha = TestClient(app, raise_server_exceptions=False)
    
    mocker.patch(
        "app.main.ClassificadorEva.calcular_indice_maturidade",
        side_effect=Exception("Erro interno simulado")
    )
    dados = ClassificacaoFactory.criar()
    response = client_falha.post("/api/classificar", json=dados)
    assert response.status_code == 500