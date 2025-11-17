# Desafio 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Com isso US$1,00 = R$5.50

n1 = float(input("Digite o seu valor em Reais(R$):"))
usd = n1*5.5

print(f'A conversao do seu dinheiro para Dólar é:{usd:.2f}US$')

