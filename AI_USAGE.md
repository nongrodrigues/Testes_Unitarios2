# Relatório de Transparência e Uso de IA

## Ferramenta Utilizada
* LLM (Modelo de Linguagem): **DeepSeek** (modelo de chat e raciocínio).

## Contexto do Projeto
O sistema desenvolvido é o **Classificador de Maturação EVA**, que avalia o nível de complexidade, violência e temas adultos do anime *Neon Genesis Evangelion* para recomendar a classificação indicativa (Acesso Liberado, com Supervisão ou Bloqueado) baseada na idade e maturidade do usuário.

## Escopo de Uso
* Geração inicial da estrutura de pastas e configuração do ambiente com `uv`.
* Auxílio na escrita dos seletores semânticos do Playwright (`get_by_label`, `get_by_role`) para os testes E2E.
* Criação do script de testes de carga (`locustfile.py`) e das métricas de SLA.
* Geração do boilerplate dos testes de integração utilizando Faker (pt_BR).

## Auditoria e Validação
* A lógica de negócio (`ClassificadorEva`) foi escrita e mantida manualmente, servindo como base de verdade para a validação da IA.
* O código gerado foi auditado para resolver conflitos de dependência (Starlette/httpx2) e problemas de renderização de template (Jinja2).
* Todos os testes foram executados localmente na máquina do desenvolvedor, atingindo a marca de **48 testes passando (100% de sucesso)**, garantindo que o uso da IA não introduziu regressões ou falhas de segurança.
* A acessibilidade foi validada por ferramenta externa (Axe-core), garantindo que a IA não gerou código HTML inacessível.