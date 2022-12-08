from open_project import open_project
from init_projetos import init_projetos
from timer import timer
import pandas as pd


file = 'Projetos.xlsx'
#init_projetos(file)
dataset = pd.read_excel(file, index_col=0)
process, projeto = open_project(dataset)
time = timer(process)
time += time
print(time)
print(projeto)
