#Saudacao
print("Saudacao")
nome = input ("Qual o seu nome?: ")
print('Olá "', nome, '"')
print('Olá "'+ nome +'"') # + é a concatenação de strings
reset = '\033[0;0m'
amarelo = '\033[1;93m'
print(f'Olá {amarelo}{nome}{reset}')