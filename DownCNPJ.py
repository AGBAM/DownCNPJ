from bs4 import BeautifulSoup
import requests
import os
url='https://arquivos.receitafederal.gov.br/dados/cnpj/dados_abertos_cnpj/'

def All(date=None,path=None):
    response = requests.get(url+periodo+"/")

    # Analisar o conteúdo HTML com BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar todos os elementos <a> com atributo href
    links = soup.find_all('a', href=True)

    # Criar uma lista com todos os hrefs
    hrefs = [link['href'] for link in links]

    hrefs=hrefs[4:]

    for h in hrefs:
        # URL do arquivo CSV
        url = 'https://dadosabertos.rfb.gov.br/CNPJ/dados_abertos_cnpj/'+periodo+"/"+h
        
        # Caminho onde você deseja salvar o arquivo
        pasta_destino = path
        nome_arquivo = h
        
        # Caminho completo do arquivo
        caminho_completo = os.path.join(pasta_destino, nome_arquivo)
        
        # Fazer o download do arquivo
        response = requests.get(url)
        
        # Salvar o arquivo
        with open(caminho_completo, 'wb') as file:
            file.write(response.content)
        
        print(f'Arquivo salvo em: {caminho_completo}')

    return