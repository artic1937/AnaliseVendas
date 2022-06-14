import pandas as pd

lista_meses=['janeiro','fevereiro','março','abril','maio','junho']

for mes in lista_meses:
    
    tabelas_vendas= pd.read_excel(f'D:/pyton/vendas em python/{mes}.xlsx')
   
    if(tabelas_vendas['Vendas']>55000).any():
    
        vendedor = tabelas_vendas.loc[tabelas_vendas['Vendas']>55000, 'Vendedor'].values[0]
        vendas = tabelas_vendas.loc[tabelas_vendas['Vendas']>55000,'Vendas'].values[0]
        print(f' alguem em {mes} faturou mais de 55000. Vendedor:{vendedor}, Vendas:{vendas}')















#Passo a passo da solução
#Abrir os 6 arquivos do excel
#Para cada arquivo:
#verificar se algum valor na coluna vendas daquele arquivo é maior que 55000
#se for maior que 55000, enviar um sms para 24 99207-9553 com o nome, o mês e as vendas do vendedor