import requests
from pprint import pprint
from get_token import token

_print = print
print = pprint

# Realizar um requisição no link para pegar os dados de um aluno em específico
url = 'http://127.0.0.1:3001/alunos/2'

headers = {
    # 'Authorization': token
}

aluno_data = {}

response = requests.get(url=url, json=aluno_data, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print(response.status_code)
    print(response.reason)

    response_data = response.json()
    print(response_data)
    print(response_data['nome'])
    print(response_data['email'])

else:
    # Erros
    print(response.status_code)
    print(response.reason)
    print(response.text)


