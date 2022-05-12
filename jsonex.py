import json
import os
"""
pessoas = [
    {
        "nome": 'Maria',
        "sobrenome": 'Vieira',
        "idade": 25,
        "ativo": False,
        "notas":['A', 'A+'],
        "telefones": {
            "residencial": "00 0000-0000",
            "celular": "00 0000-0000"
        }

    },
    {
        "nome": 'Joana',
        "sobrenome": 'Moreira',
        "idade": 32,
        "ativo": True,
        "notas":['B', 'A'],
        "telefones": {
        "residencial": "00 1000-0000",
        "celular": "00 1000-0000"
        }
    },
]

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'arquivo-python.json')

with open(SAVE_TO, 'w') as file:
    json.dump(pessoas, file, indent=2)


print(json.dumps(pessoas, indent=2))"""

# para ler
BASE_DIR = os.path.dirname(__file__)
JSON_FILE = os.path.join(BASE_DIR, 'arquivo-python.json')

with open(JSON_FILE, 'r') as file:
    pessoas = json.load(file)
    print(pessoas)

    for pessoa in pessoas:
        print(pessoa['nome'])
