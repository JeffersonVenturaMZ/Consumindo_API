import requests
from pprint import pprint
from get_token import token

_print = print
print = pprint

# Realizar uma requisição no link para pegar os dados de todos os alunos
url = 'http://127.0.0.1:3001/alunos'

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

    for aluno in response_data:
        print(aluno)
        
else:
    # Erros
    print(response.status_code)
    print(response.reason)
    print(response.text)


