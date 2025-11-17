#Desafio 008 - Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e em milímetros.

n1 = float(input('Digite um valor em metros:'))
cent = n1*100
mili = n1*1000

print(f'O valor em centimetros é:{cent:.2f} cm. \nO valor em milímetros é:{mili:.2f} mm')