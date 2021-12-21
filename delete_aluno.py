import requests
from pprint import pprint
from get_token import token

_print = print
print = pprint

# Request no link com o ID do aluno que deseja excluir
url = 'http://127.0.0.1:3001/alunos/3'

headers = {
    'Authorization': token
}

aluno_data = {}

response = requests.delete(url=url, json=aluno_data, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print(response.status_code)
    print(response.reason)

    response_data = response.json()
    print(response_data)

else:
    # Erros
    print(response.status_code)
    print(response.reason)
    print(response.text)
