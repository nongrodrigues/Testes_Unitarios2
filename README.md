# Classificador de Maturação EVA

Este projeto é uma aplicação web de classificação indicativa baseada no universo de **Neon Genesis Evangelion**. O sistema avalia o nível de complexidade psicológica, violência e temas adultos do conteúdo para determinar se um espectador tem idade e maturidade suficientes para assisti-lo.

A aplicação foi construída com **FastAPI**, **Pydantic** e interface **HTML/JS**, e conta com uma suíte de **48 testes automatizados** (Unitários, Integração, E2E, Acessibilidade WCAG 2.1 AA e Carga).

**Comando executado:**
`uv run locust -f locustfile.py --headless -u 50 -r 5 -t 30s --host http://127.0.0.1:8000`

**Métricas Coletadas (Locust):**
* **Vazão (RPS):** 22.14 requisições por segundo.
* **Tempo de Resposta p95:** 30 ms (Agregado) e 49 ms (Rota /api/classificar).
* **Taxa de Falhas:** 0.00% (Zero falhas em 651 requisições).
* *Nota de Auditoria:* O SLA configurado no script exige tempo de resposta inferior a 200ms. O sistema entregou um p95 de 49ms na rota principal, provando a alta eficiência de desempenho (ISO/IEC 25010).

### 🧪 Resultados dos Testes Automatizados
* **Testes Unitários:** 42 passed
* **Testes de Integração (Mocks/Faker):** 3 passed
* **Testes E2E e Acessibilidade (Playwright/Axe):** 3 passed
* **Total:** 48 passed in 4.57s