import os


def open_project(dataset):

    cmd = 'code .'
    print(dataset)
    index = int(input('Select the project to work by index: '))
    if index > dataset.shape[0]:
        raise "Invalid index"
    path = dataset['path'].iloc[index]
    projeto = dataset['projetos'].iloc[index]
    if path == 'empty':
        os.system(cmd)
        return ('"Code.exe"', projeto)
    else:
        cmd = 'pycharm64.exe ' + path + '\\main.py'
        os.system(cmd)
        return ('"pycharm64.exe"', projeto)
