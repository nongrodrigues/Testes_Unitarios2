# PRD - Classificador de Maturação EVA

## 1. Visão Geral
O sistema tem como objetivo classificar a maturidade de conteúdo de Neon Genesis Evangelion com base em três notas (Violência, Complexidade Psicológica e Temas Adultos), determinando se o usuário tem idade e maturidade para assistir.

## 2. Rotas da API
* `GET /`: Retorna a interface HTML do formulário.
* `POST /api/classificar`: Recebe as notas e a idade, e retorna o índice, acesso e permissão.
* `GET /health`: Verifica a saúde da aplicação.

## 3. Interface Web
* Página única contendo um formulário com campos para Nota 1, Nota 2, Nota 3 e Idade.
* Botão "Calcular Classificação".
* Exibição do resultado dinâmico via JavaScript (role="status").

## 4. Requisitos Não Funcionais Avaliados
* **Acessibilidade:** O sistema deve estar em conformidade com a WCAG 2.1 AA (validado via Axe-core).
* **Performance:** O tempo de resposta p95 da API de classificação deve ser inferior a 200ms sob carga de 50 usuários simultâneos.
* **Confiabilidade:** A aplicação deve retornar HTTP 422 para dados inválidos e HTTP 200 para sucesso.