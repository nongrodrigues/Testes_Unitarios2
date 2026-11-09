from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from app.services import ClassificadorEva

app = FastAPI(title="Classificador EVA")
templates = Jinja2Templates(directory="app/templates")

class ClassificacaoRequest(BaseModel):
    n1: float = Field(..., ge=0.0, le=10.0)
    n2: float = Field(..., ge=0.0, le=10.0)
    n3: float = Field(..., ge=0.0, le=10.0)
    idade: int = Field(..., ge=0)

class ClassificacaoResponse(BaseModel):
    indice: float
    acesso: str
    permissao_idade: str

@app.get("/", response_class=HTMLResponse)
def pagina_inicial(request: Request):
    # Correção para a nova versão do Starlette:
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/api/classificar", response_model=ClassificacaoResponse)
def classificar(payload: ClassificacaoRequest):
    indice = ClassificadorEva.calcular_indice_maturidade(payload.n1, payload.n2, payload.n3)
    acesso = ClassificadorEva.determinar_acesso(indice)
    permissao = ClassificadorEva.verificar_idade(payload.idade)
    return ClassificacaoResponse(indice=indice, acesso=acesso, permissao_idade=permissao)