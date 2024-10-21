from flask import Flask, request, jsonify
import base64
from PIL import Image
import io

app = Flask(__name__)

@app.route('/processar-imagem', methods=['POST'])
def processar_imagem():
    dados = request.get_json()

    if 'imagem' not in dados or 'nome_arquivo' not in dados:
        return jsonify({"error": "Dados inválidos, imagem ou nome do arquivo ausente"}), 400

    try:
        # Decodificar a string base64
        imagem_base64 = dados['imagem']
        imagem_bytes = base64.b64decode(imagem_base64)
        
        # Abrir a imagem usando o PIL
        imagem = Image.open(io.BytesIO(imagem_bytes))
        
        # Processar a imagem (exemplo: redimensionar)
        imagem = imagem.resize((300, 300))
        
        # Salvar a imagem processada
        caminho_otimizado = 'imagem_otimizada.jpg'
        imagem.save(caminho_otimizado, 'JPEG', quality=85)
        
        return jsonify({"message": "Imagem processada com sucesso"}), 200

    except Exception as e:
        return jsonify({"error": f"Ocorreu um erro inesperado: {str(e)}"}), 500

@app.route('/', methods=['GET'])
def home():
    return "Bem-vindo ao serviço Flask!"


if __name__ == '__main__':
    app.run(debug=True)
