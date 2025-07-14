from cryptography.fernet import Fernet
import os

def gerar_chave():
    return Fernet.generate_key()

def criptografar_arquivo(chave, arquivo_entrada, arquivo_saida):
    fernet = Fernet(chave)
    
    with open(arquivo_entrada, 'rb') as file:
        dados = file.read()
    
    dados_criptografados = fernet.encrypt(dados)
    
    with open(arquivo_saida, 'wb') as file:
        file.write(dados_criptografados)
    
    print(f"Arquivo criptografado com sucesso! Salvo como {arquivo_saida}")
    print(f"Chave de criptografia: {chave.decode()}")
    print("Salve esta chave em um local seguro! Você precisará dela para descriptografar o arquivo.")

def configPrincipal(entrada):
    # Gerar chave
    chave = gerar_chave()
    
    # Criptografar o arquivo
    arquivo_entrada = str(entrada)
    arquivo_saida = 'file.encrypted'
    
    criptografar_arquivo(chave, arquivo_entrada, arquivo_saida)

if __name__ == "__main__":
    configPrincipal('teste.py')
