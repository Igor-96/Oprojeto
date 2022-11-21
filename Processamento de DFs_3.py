#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 16:12:12 2022

@author: rila
"""

import pandas as pd

file1 = '/home/rila/Área de Trabalho/O PROJETO/COMODITES LIST.ods'

df1 = pd.read_excel(file1)

df1 = df1.apply(lambda x: x.str.strip().str.lower())

df1 = df1.drop_duplicates()

lista =[]

for i in df1['Comodites']:
    lista.append(len(i))
    
df1['lista'] = lista

df1 = df1[df1.lista > 2]

df1 = df1.drop(['lista'], axis=1)

    
#df1 = df1.iloc[df1['Comodites'] > 2 ]
        
#df1.drop(df1[len(df1['Comodites']) < 2].index)

df1.to_excel('/home/rila/Área de Trabalho/O PROJETO/COMODITES.ods')


