#AUGUSTO Z. VITALI - 2190
profits = []
expenses = []

while True:
    profit = float(input('Digite o lucro desse mês: '))
    expense = float(input('Digite a despesa desse mês: '))
    profits.append(profit)
    expenses.append(expense)
    opcao = input('Deseja inserir novamente? S/N: ').upper().strip()
    if opcao == 'N':
        break
    else:
        continue

monthly_revenues = list(map(lambda x,y: x-y , profits,expenses))
annual_revenue = sum(monthly_revenues)/len(monthly_revenues)
print(f'Lucro de cada mês: {monthly_revenues}')
print(f'O lucro médio mensal é de R${annual_revenue:.2f}')
loss_months = list(filter(lambda x: x < 0 , monthly_revenues))
print(f'Meses de prejuízo: {loss_months}')