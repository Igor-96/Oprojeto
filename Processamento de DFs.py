#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 16:12:12 2022

@author: rila
"""

import pandas as pd

file1 = '/home/rila/Área de Trabalho/O PROJETO/chemical_elements_2_wiki.ods'
file2 = '/home/rila/Área de Trabalho/O PROJETO/commodity_filtered_conv.ods'

df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)

df1.columns = df1.columns.str.strip()
df2.columns = df2.columns.str.strip()
df1['Symbol'] = df1['Symbol'].apply(lambda x: x.strip().lower())
df2['value'] = df2['value'].apply(lambda x: x.strip().lower())

df1['Comodites'] = df2['value']

valores = []
valores.append()

for i in df1.itertuples():
    valores.append(i.Comodite if i.Symbol == i.Comodites else 'no')

df2['Novos'] = valores
print(df2['Novos'])

