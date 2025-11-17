# Desafio 012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5¢ de desconto.

produto = float(input("Digite o preço do produto desejado:"))
desc1 = produto * 0.05
desc2 = produto - desc1

print(f'O valor do produto com 5% de desconto é: {desc2:.2f}')
