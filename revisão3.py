alunos = [
    {"nome": "Jhemeson", "email": "jhemeson@gmail.com", "idade": 18, "curso": "CCP"},
    {"nome": "Julio", "email": "julio@gmail.com", "idade": 19, "curso": "CCP"},
    {"nome": "Carlos", "email": "carlos@gmail.com", "idade": 22, "curso": "ADS"}
]

maior = []
menor = []
motivos = []

for aluno in alunos:
    if aluno["idade"] >= 18:
        maior.append(aluno["idade"])
    else:
        menor.append(aluno["idade"])

print (maior)
print (menor)