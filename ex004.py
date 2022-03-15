#Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

palavra = input("Digite qualquer coisa:")

print('Eh alfanumerico?', palavra.isalnum())
print('Eh alfa?', palavra.isalpha())
print('Eh ascii?', palavra.isascii())
print('Eh um digito?', palavra.isdigit())
print('Eh minusculo?', palavra.islower())
print('Eh decimal?', palavra.isdecimal())
print('Eh identificador?', palavra.isidentifier())
print('Eh numerico?', palavra.isnumeric())
print('Eh printavel?', palavra.isprintable())
print('Eh espaço?', palavra.isspace())
print('Eh titulo?', palavra.istitle())
print('Eh maiusculo?', palavra.isupper())
