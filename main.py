import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACacbbdacef693f8ce9b6b8fef90c8c49e"
# Your Auth Token from twilio.com/console
auth_token  = "ea41efa45024f1d5ae8277a7a96a5770"

client = Client(account_sid, auth_token)

# Passo a passo de solução

# Abrir os 6 arquivos em Excel

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses: 
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0] 
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}') 




message = client.messages.create(
    to="+5517992100660", 
    from_="+16084203176",
    body=f'Parabéns {vendedor}, em {mes} você bateu a meta, com o total de {vendas}')

print(message.sid)


# .any() no final serve para ver se algum valor naquela coluna é maior de 55 mil, não a coluna inteira.

# Para cada arquivo:

# Verificar se algum vendedor vendeu mais que R$ 55.000,00


# Se for maior -> sms com nome/mes/vendas

# Se for menor -> nada.