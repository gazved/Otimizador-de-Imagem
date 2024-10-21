import base64
import requests

# Caminho para a imagem
caminho_imagem = 'HomePic.jpg'

# Ler a imagem e converter para base64
with open(caminho_imagem, 'rb') as img_file:
    imagem_base64 = base64.b64encode(img_file.read()).decode('utf-8')

# Dados a serem enviados no JSON   
dados = {
    'imagem': imagem_base64,
    'nome_arquivo': 'HomePic.jpg'
}

# Enviar a requisição para o servidor Flask
response = requests.post('http://localhost:5000/processar-imagem', json=dados)

# Mostrar a resposta do servidor
print(response.json())
