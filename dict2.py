turma = [
{"nome": "Ana", "Idade": 16, "Nota": 8,5},
{"nome": "Bruno", "Idade": 17, "Nota": 7,0},
{"nome": "Carla", "Idade": 16, "Nota": 9,5},
]

print (turma[0]["nome"])
print (turma[2]["nota"])

print("---RELATORIO DA TURMA---")
for aluno in turma:
  print(f"Nome: {aluno['nome]} | Nota: {aluno['nota']}")
