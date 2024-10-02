#AUGUSTO Z. VITALI - 2190
funcionarios = {}
while True:
    nome = input('Nome do funcionário: ').lower().capitalize()
    salario  = float(input('Salário do funcionário: '))
    funcionarios[nome] = salario
    opcao = input('Deseja inserir novamente? S/N: ').upper().strip()
    if opcao == 'N':
        break
    else:
        continue

for nome,salario in funcionarios.items():
    print(f'{nome}: {salario:.2f}')

salario_alto = float(input('Digite um salário, todos os valores acima serão filtrados e recerão aumento: '))
funcionarios_salario_alto = dict(filter(lambda x: x[1] > salario_alto, funcionarios.items())) #Filter não precisa falar a chave/nome pois só filtra, retorna o dicionário em si, só filtrando
aumento = dict(map(lambda x: (x[0], x[1]*1.15) , funcionarios_salario_alto.items()))  #A vírgula depois do x[0] é pra fazer o dicionário (sendo x[0] o nome e x[1] o salário)
print(f'Salários após aumento: {aumento}')

soma_salarios = sum(funcionarios.values())
media_salarial_empresa = soma_salarios/len(funcionarios)
print(f'Média salarial da empresa: {media_salarial_empresa}')

print(f'Maior salário da empresa: {max(funcionarios.values())}, menor salário: {min(funcionarios.values())}')




