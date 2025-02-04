coisa = input('Digite alguma coisa: ')
print('O tipo de dado escrito é: ', (type(coisa)))
print('O dado é numérico? ', (coisa.isnumeric()))
#Funções (métodos) devem sempre vir acompanhadas de parênteses. 
print('O dado  é alfabético? {}'.format(coisa.isalpha()))
print('O dado é alfanumérico? ', (coisa.isalnum()))
print('O dado está em letras maiúsculas? ', (coisa.isupper()))
print('O dado está em letras minúsculas? ', (coisa.islower()))
print('O dado contém apenas espaços? ', (coisa.isspace()))
print('O dado está capitalizado? ', (coisa.istitle()))
# Capitalizada, quando há maiúsculas (No início) e minúsculas 
# Coisa é um objeto, pois possuí características (atributos) e realiza funcionalidades (métodos).