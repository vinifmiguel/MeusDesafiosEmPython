# Desafio 013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento!

salario = float(input('Digite o seu salário atual R$:'))
novo = salario + (salario * 15/100)


print(f'Seu salário novo com acréscimo de 15% é: R${novo:.2f}')

