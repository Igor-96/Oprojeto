#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 16:12:12 2022

@author: rila
"""

import pandas as pd

file1 = '/home/rila/Área de Trabalho/O PROJETO/COMODITES2.ods'
df1 = pd.read_excel(file1)
file2 = '/home/rila/Área de Trabalho/O PROJETO/chemical_elements_2_wiki.ods'
df2 = pd.read_excel(file2)

df2.columns = df2.columns.str.strip()
df2['Name'] = df2['Name'].apply(lambda x: x.strip().lower())

df1['name'] = df2['Name']
df1['desc'] = df2['Description']


valores = []

for i in df1.itertuples():
    valores.append(i.desc if i.Comodites in df1['name'] else 'Não-Elemento')
    
df1['Novos'] = valores
print(df1['Novos'])