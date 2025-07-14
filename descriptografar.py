from cryptography.fernet import Fernet
import sys

def descriptografar_arquivo(chave, arquivo_entrada, arquivo_saida):
    try:
        fernet = Fernet(chave)
        
        with open(arquivo_entrada, 'rb') as file:
            dados_criptografados = file.read()
        
        dados_descriptografados = fernet.decrypt(dados_criptografados)
        
        with open(arquivo_saida, 'wb') as file:
            file.write(dados_descriptografados)
        
        print(f"Arquivo descriptografado com sucesso! Salvo como {arquivo_saida}")
    except Exception as e:
        print(f"Erro ao descriptografar: {str(e)}")
        print("Verifique se a chave fornecida está correta.")

def main():
    if len(sys.argv) != 2:
        print("Uso: python descriptografar.py <chave>")
        print("Exemplo: python descriptografar.py 7mnOVtrANQR_78EUiHvvwRQXycyOnVtjQRdSQekSAUc=")
        return
    
    chave = sys.argv[1].encode()
    arquivo_entrada = 'file.encrypted'
    arquivo_saida = 'file.py'
    
    descriptografar_arquivo(chave, arquivo_entrada, arquivo_saida)    

if __name__ == "__main__":
    main()
