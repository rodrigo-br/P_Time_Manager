import pandas as pd
import openpyxl
import os

file = 'Projetos.xlsx'
projetos = []
tempo = []

print(pd.read_excel(file, index_col=0))

while True:
    projeto = input("Digite o nome de um novo projeto (deixe em branco para encerrar)")
    if not projeto:
        break
    projetos.append(projeto)
    tempo.append(0)
    ds = {'projetos': projetos, 'tempo': tempo}
    dataframe = pd.DataFrame(ds)

if not os.path.exists(file):
    dataframe.to_excel(file, index_col=0)

elif projetos:
    data_antigo = pd.read_excel(file, index_col=0)
    novo_data = pd.concat([data_antigo, dataframe], ignore_index=True)
    novo_data.to_excel(file)

print(pd.read_excel(file, index_col=0))
