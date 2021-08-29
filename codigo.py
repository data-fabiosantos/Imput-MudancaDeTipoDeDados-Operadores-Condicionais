
# Imput
nome = input("Por favor, digite o seu nome: ")

print("Olá, seja bem-vindo", nome)

# é possível incluir separador dentro do print, como também pula linha: end
# (sep='=>', end='\n\n\n')


# Exercicio 

# Exercício de fixação 1: Elabore um programa que solicite ao usuário,  
# separadamente, seu nome e sobrenome e mostre a mensagem: “Seu nome completo: # Nome Sobrenome.”, com um espaço na junção dos nomes e um ponto no final, sem # pular linha.

# Resolução 

nome = input("Por favor, digite o seu nome: ")
sobrenome = input("Por favor, digite o seu sobrenome: ")
print("Seu nome completo: "+nome+" "+sobrenome+".")


# Conversão de Tipo de dado
num1 = input("Por favor, digite o primeiro número: ")
num2 = input("Por favor, digite o segundo número: ")
soma = num1 + num2
print("A soma dos números é ", soma)


# Necessário adicionar o Int() para alterar de String para interno. 
num1 = int(input(("Por favor, digite o primeiro número: "))
num2 = int(input("Por favor, digite o segundo número: "))
soma = num1 + num2
print("A soma dos números é ", soma)

# Funções para mudança de tipo de dados simples
# int()	Converte um dado para um número do tipo inteiro.
# float()	Converte um dado para um número do tipo ponto flutuante (com casas 
# decimais).
# complex()	Converte um dado para um número complexo.
# str()	Converte um dado para sua versão string.

# Formatação de saída de dados com o operador de modulação

num = 6/7

print(num)

# Documentação no Google docs 
# https://docs.google.com/document/d/1hskRQlprEgsMtT3Q7QfBVoyGbq5MKXe9DM_Os9J_jX8/edit 


'''Solicite ao usuário dois produtos, com suas respectivas quantidades e preços e mostre esses dados formatados como tabelas.'''

prod1 = input("Digite o nome do primeiro produto: ")
quant1 = int(input("Digite a quantidade do primeiro produto: "))
valor1 = float(input("Digite o valor do primeiro produto: "))
prod2 = input("Digite o nome do segundo produto: ")
quant2 = int(input("Digite a quantidade do segundo produto: "))
valor2 = float(input("Digite o valor do segundo produto: "))
print(f'{"Produto":20}|{"Quantidade":^12}|{"Valor":>10}')
print(f'{prod1:20}|{quant1:^12}|{valor1:10.2f}')
print(f'{prod2:20}|{quant2:^12}|{valor2:10.2f}')


# Estrutura condicionais

# Operadores 

# ==	Compara se dois dados são iguais.
# !=	Compara se dois dados são diferentes.
# <	Compara se um valor é menor que outro.
# >	Compara se um valor é maior que outro.
# <=	Compara se um valor é menor ou igual a outro.
# >=	Compara se um valor é maior ou igual a outro.


'''um programa que solicite ao usuário seu ano de nascimento e calcule sua idade. Para ser mais assertivo, também deve perguntar se o usuário já fez aniversário neste ano e analisar a influência dessa informação no cálculo da idade.'''


# Como funcionará a lógica
# início
#     inteiro: nascimento, idade, ano_atual;
#     texto: resp;
#     ano_atual <- 2020;
#     escreva ("Qual é o seu ano de nascimento?");
#     leia (nascimento);
#     idade <- anoAtual – nascimento;
#     escreva ("Você já fez aniversário neste ano?");
#     leia(resp);
#     se (resp = "não")
#         então
#             idade <- idade – 1;
#     fimse;
#     escreva ("Sua idade é ", idade);
# fim.


#Construção do código em Python
ano_atual = 2020
nascimento = int(input("Qual é o seu ano de nascimento? "))
idade = ano_atual - nascimento
resp = input("Você já fez aniversário neste ano? ")
if resp == "Não":
    idade -= 1
print("Sua idade é", idade)


# seleção simples
'''Elabore um programa que solicite ao usuário as notas de determinada disciplina escolar e calcule a média. Se a média for maior ou igual a 7, deve mostrar ao aluno que ele foi aprovado.'''


# Como funcionará a lógica
# início
#     real: nota1, nota2, nota3, nota4, media;
#     escreva ("Digite as 4 notas bimestrais da disciplina: ");
#     leia (nota1, nota2, nota3, nota4);
#     media = (nota1 + nota2 + nota3 + nota4) / 4;
#     escreva ("Sua média na disciplina foi ", media);
#     se (media >= 7)
#         então
#             escreva ("Você está aprovado na disciplina!");
#     fimse;
# fim.


#Construção do código em Python
print("Digite as 4 notas bimestrais da disciplina: ")
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())
media = (nota1 + nota2 + nota3 + nota4) / 4
print("Sua média na disciplina foi", media)
if media >= 7:
    print("Você está aprovado na disciplina!")


# seleção composta
'''Elabore um programa que solicite ao usuário as notas de determinada disciplina escolar e calcule a média. Se a média for maior ou igual a 7, deve mostrar ao aluno que ele foi aprovado; caso contrário, que foi reprovado.'''


# início
#     real: nota1, nota2, nota3, nota4, media;
#     escreva ("Digite as 4 notas bimestrais da disciplina: ");
#     leia (nota1, nota2, nota3, nota4);
#     media = (nota1 + nota2 + nota3 + nota4) / 4;
#     escreva ("Sua média na disciplina foi ", media);
#     se (media >= 7)
#         então
#             escreva ("Você está aprovado na disciplina!");
#         senão
#             escreva ("Você reprovou na disciplina!");
#     fimse;
# fim.


#Construção do código em Python
print("Digite as 4 notas bimestrais da disciplina: ")
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())
media = (nota1 + nota2 + nota3 + nota4) / 4
print("Sua média na disciplina foi", media)
if media >= 7:
    print("Você está aprovado na disciplina!")
else:
    print("Você reprovou na disciplina!")


# seleção encadeada
'''Elabore um programa que solicite três números diferentes ao usuário e informe qual deles é o menor.'''

# início
#     inteiro: num1, num2, num3;
#     escreva ("Digite três números diferentes: ");
#     leia (num1, num2, num3);
#     se (num1 < num2)
#         então
#             se (num1 < num3)
#                 então
#                     escreva ("O primeiro número é o menor!");
#                 senão
#                     escreva ("O terceiro número é o menor!");
#             fimse;
#         senão
#             se (num2 < num3)
#                 então
#                     escreva ("O segundo número é o menor!");
#                 senão
#                     escreva ("O terceiro número é o menor!");
#             fimse;
#     fimse;


#Construção do código em Python
print("Digite três números diferentes: ")
num1 = float(input())
num2 = float(input())
num3 = float(input())
if num1 < num2:
    if num1 < num3:
        print("O primeiro número é o menor!")
    else:
        print("O terceiro número é o menor!")
else:
    if num2 < num3:
        print("O segundo número é o menor!")
    else:
        print("O terceiro número é o menor!")

# Fim
