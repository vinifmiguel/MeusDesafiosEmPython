#Desafio 007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média!

nota1 = float(input('Digite sua primeira nota escolar:'))
nota2 = float(input('Digite sua segunda nota escolar:'))
media= (nota1+nota2)/2
print(f'A média entre {nota1} e {nota2} é igual a:{media:.1f}')
