#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 16:12:12 2022

@author: rila
"""

import pandas as pd

file1 = '/home/rila/Área de Trabalho/O PROJETO/teste1.ods'

df1 = pd.read_excel(file1)

valores = []

for i in df1.itertuples():
    valores.append(i.Name if i.Comodites in df1['Symbol'] else i.Comodites)

df2['Novos'] = valores
print(df2['Novos'])

