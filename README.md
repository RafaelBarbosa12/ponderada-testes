# Teste Automatizado da API de Especialidades

Este repositório contém um teste automatizado para a criação de uma especialidade.

## Caso de Teste

### Objetivo
Verificar se o controller de especialidade permite criar uma especialidade corretamente.

### Pré-condição
- A API deve estar em execução em `http://localhost:3000`.
- O endpoint `/especialidades` deve estar disponível.

### Procedimento de Teste
1. Enviar uma requisição `POST` para o endpoint `/especialidades` com o nome de uma nova especialidade.
2. Verificar se a resposta possui o status `201` e o nome da especialidade correta.

### Resultado Esperado
- Status das respostas:
  - `POST /especialidades`: `201 Created`

### Resultado Obtido

Ao abrir o banco de dados, a informormação adicionada para a especialidade foi corretamente armazenada.