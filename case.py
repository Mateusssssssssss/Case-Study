import pandas as pd
import numpy as np
import statistics as st
#ler o CSV
data = pd.read_csv('case_estagio.csv')
#Informações sobre a tabela
descricao = data.describe()
#limite de linhas a serem exibidas
limite = data.head(50)
#Filtro por Categoria de vendas
filtro_item =data['product_category_name'].value_counts()
#filtro De vendas por ID do vendedor
filtro_vendas =data['seller_id'].value_counts()
# Filtro para status do pedido e a quantidade
filtro_status =data['order_status'].value_counts()
#numero de vendedores
vendedores_unicos = len(set(filtro_vendas))
#5 Categorias mais Vendidas
category_sales = filtro_item.head(5)
#5 Vendedores com maior numero de vendas
sales_five = filtro_vendas.head(5)
#Numero total de vendas
maximo = sum(filtro_vendas)
#Mediana de vendas
mediana = st.median(filtro_vendas)
#media de vendas
media = maximo / vendedores_unicos
#Desvio padrão
desvio_padrao = st.stdev(filtro_vendas)
#tirar todos valores nulos
null = filtro_item.dropna()
#conta o filtro de vendas sem valores null, e retorna a quantidade
contar = null.count()
#conta o filtro de vendas sem função de tirar valores nulls
contar1 = filtro_vendas.count()

print(f'Categorias Com Mais Vendas:\n{category_sales}')
print('-------------------------------------------------')
print(f'Numero de Vendedores: {vendedores_unicos}')
print(f'ID.s dos 5 Maiores Vendedores e Quantidade de Vendas:\n{sales_five}')
print('-------------------------------------------------')
print(f'Media de vendas por vendedor: {media}\nmediana de vendas totais: {mediana}\nDesvio Padrão: {desvio_padrao}')
print(f'Numero Total de Vendas: {maximo}')
print('-------------------------------------------------')
