#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 18:37:57 2022

@author: rila
"""

import pandas as pd

file_principal = '/home/rila/Área de Trabalho/O PROGETO/file_principal_filtragem.ods'
file_novo = '/home/rila/Área de Trabalho/O PROGETO/comodite_test1.ods'
df_principal = pd.read_excel(file_principal)
df_novo = pd.read_excel(file_novo)

#novos_valores = [i for i in df_novo["value"]]

df_novo['value'] = df_novo['value'].apply(lambda x: x.strip().lower())

novos_valores = df_novo["value"]

df_principal["Comodites"] = df_principal["Comodites"].append([novos_valores])

for i in df_principal.itertuples():
    valores.append(i.Name if i.Comodites in df_principal['Symbol'] else i.Comodites)

df_principal = df_principal.apply(lambda x: x.str.strip().str.lower())

print(df_principal)