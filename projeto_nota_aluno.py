nomeAluno = str(input("Digite o nome do aluno: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
faltas = float(input("Digite a quantidade de faltas: "))

media = (nota1 + nota2) / 2
if media < 7 or faltas > 3:
    print("O aluno: ",nomeAluno," esta Reprovado!")
else:
    print("O aluno: ",nomeAluno," esta Aprovado!!!")