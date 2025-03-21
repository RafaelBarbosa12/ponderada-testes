import requests

# URL da API
url = "http://localhost:3000/especialidades"

# Dados da especialidade para cadastro
payload = {
    "nome": "Cardiologia"
}

# Enviar requisição POST
response = requests.post(url, json=payload)

# Verificar o status da resposta
if response.status_code == 201:
    print("Teste PASS: Status 201 recebido.")
else:
    print(f"Teste FAIL: Status {response.status_code} recebido.")

# Verificar o corpo da resposta
expected_data = {
    "id": 1,
    "nome": "Cardiologia"
}

if response.json() == expected_data:
    print("Teste PASS: Dados da especialidade corretos.")
else:
    print("Teste FAIL: Dados da especialidade incorretos.")