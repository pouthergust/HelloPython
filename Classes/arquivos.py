import os
from pathlib import Path

# ROOT_PATH = 
path = Path(__file__).parent.parent

os.mkdir(path / "novo_diretorio")

novo_arquivo = open(path / "novo_diretorio", "w")

# novo_arquivo.write("Linha 1\n") # Adciona um linha
# novo_arquivo.writelines(['Linha 2', 'Linha 3']) # Recebe um iteravel e adiciona o conteudo, sendo cada linha um indice do iteravel

novo_arquivo.close()

# arquivo = open(path, 'r')

# print(arquivo.read())      # Retorna a string de todo o arquivo
# print(arquivo.readline())  # Retorna uma linha por vez
# print(arquivo.readlines()) # Retorna uma lista contendo cada linha do arquivo

# arquivo.close()