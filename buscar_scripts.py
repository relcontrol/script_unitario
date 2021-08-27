# -*- coding: utf-8 -*-
"""
Created on Sat May 25 12:36:00 2019

@author: 145100
"""

from os import walk
from os.path import join, splitext, basename

#todos os arquivos

arquivos = []


sintaxes = r'M:\PASTA'

for folder, subfolders, files in walk(sintaxes):
    for f in files:
        
        if splitext(f)[1].lower() == '.py':
        
            arquivo = join(folder, f)
            arquivos.append(arquivo.lower())
               
arquivos_ricardo = list(filter(lambda x: splitext(x)[1].lower() == '.py', arquivos))

arquivos_validos = []

for arquivo in arquivos_ricardo:    
    with open(arquivo, encoding='latin') as f:
        syntax = f.readlines()
        
        for linha in syntax:
            if 'novos_cj_aceitos' in linha.lower(): #DEIXAR LOWER
                arquivos_validos.append(arquivo)
                break
                
import pandas as pd

df = pd.DataFrame({'ARQUIVOS':arquivos_validos})

