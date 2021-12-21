import requests
from pprint import pprint
from get_token import token

_print = print
print = pprint

url = 'http://127.0.0.1:3001/alunos/3'

headers = {
    'Authorization': token
}

aluno_data = {
    "nome": "José",
    "sobrenome": "Leonardo",
    "email": "joseleonardomb@email.com",
    "idade": "29",
    "peso": "78",
    "altura": "1.77"
}

response = requests.put(url=url, json=aluno_data, headers=headers)

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


