#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 18:49:52 2022

@author: rila
"""
#df_novo["value"].str.split(pat = ",", expand=True).apply(lambda x : x.value_counts(), axis = 1).fillna(0).astype(int)


import pandas as pd

file_principal = '/home/rila/Área de Trabalho/O PROGETO/tabela_atualizada_principal_2.1.ods'
file_novo = '/home/rila/Área de Trabalho/O PROGETO/lista_nova_comodite_food_detalhada_2.ods'
df_principal = pd.read_excel(file_principal)
df_novo = pd.read_excel(file_novo)

df_novo[['value', 'B']] = df_novo['value'].str.split(', ', 2, expand=True)
df_novo[['value', 'B']] = df_novo['value'].str.split(' ', 1, expand=True)
df_novo[['value', 'B']] = df_novo['value'].str.split('-', 1, expand=True)
df_novo[['value', 'B']] = df_novo['value'].str.split('/', 1, expand=True)

df_novo['value'] = df_novo['value'].map(lambda x: x.rstrip(','))

df_novo['value'] = df_novo['value'].apply(lambda x: x.strip().lower())
df_novo = df_novo.drop_duplicates()
df_principal['Name'] = df_principal['Name'].apply(lambda x: x.strip().lower())
df_principal['Comodites'] = df_principal['Comodites'].apply(lambda x: x.lower())

novos_valores = [i for i in df_novo['value']]

df2 = pd.DataFrame(novos_valores, columns=['Comodites'])

df2['Name'] = ['xx' for i in df_novo['value']]
df2['Symbol'] = ['xx' for i in df_novo['value']]

df_final = pd.concat([df_principal, df2])
df_final = df_final.fillna('xx')
df_final.reset_index(inplace = True)

lista = [i for i in df_final['Symbol']]
valores=[]

for i in df_final.itertuples():
    valores.append(i.Name if i.Comodites in lista else i.Comodites)
    
df_final['Comodites'] = valores

data2 = [len(i) for i in df_final['Comodites']]
df_final['Len'] = data2
df_final = df_final.drop(df_final[df_final.Len <= 2].index)

df_final['Comodites']  = df_final['Comodites'] .drop_duplicates()
df_final = df_final.dropna()
df_final.reset_index(inplace = True)

file_resultado = df_final.drop(columns = ['level_0', 'index'])

#file_resultado.to_excel('/home/rila/Área de Trabalho/O PROGETO/tabela_atualizada_principal_2.1.ods')

print(len(df_principal))
print(file_resultado)