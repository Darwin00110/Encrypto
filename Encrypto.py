import string
import tkinter as tk
from tkinter import Tk, filedialog
from turtle import color, width

from urllib3.exceptions import BodyNotHttplibCompatible
import criptografar
import descriptografar
from PIL import Image, ImageTk
import requests
from io import BytesIO
import os
tela = tk.Tk()
tela.title("Encrypto")
tela.geometry("300x300")
tela.config(bg="#1e2a38")

frameSelecaoArquivo = tk.Frame(tela, bg="#1e2a38", bd=3, relief="solid")
frameSelecaoArquivo.grid(padx=13, pady=30)

usuario = os.getlogin()

class emProducao:
    def producao01():
        frame = tk.Frame(tela, bg="#1e2a38", bd=3, relief="solid")
        frame.pack(pady=20)
        
        # Botão para criptografar
        # Campo para inserir o nome do arquivo
        lbl_arquivo = tk.Label(frame, text="Nome do arquivo:", bg="#1e2a38", fg="white")
        lbl_arquivo.pack(pady=5)
        
        entrada_arquivo = tk.Entry(frame, relief="solid", highlightbackground="blue", highlightthickness=2)
        entrada_arquivo.pack(pady=5)
        
        # Botão para criptografar
        btn_criptografar = tk.Button(frame, text="Criptografar", command=lambda: criptografar.configPrincipal(entrada_arquivo.get()))
        btn_criptografar.pack(pady=5)
        
        # Botão para descriptografar
        btn_descriptografar = tk.Button(frame, text="Descriptografar", command=lambda: descriptografar.main())
        btn_descriptografar.pack(pady=5)
        
        # Área para mostrar mensagens
        mensagem = tk.Label(frame, text="", bg="#1e2a38", fg="#0b5367")
        mensagem.pack(pady=10)


try:
    import os
    caminho_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_icon = os.path.join(caminho_atual, "img", "icon", "icon.ico")
    tela.iconbitmap(caminho_icon)
except Exception as e:
    print(f"Erro ao carregar ícone: {str(e)}")

texto = tk.Label(frameSelecaoArquivo, text="Arquivo", fg="white", bg="#1e2a38")
texto.grid(row=0, column=0, pady=3)
Input = tk.Entry(frameSelecaoArquivo, width=44, bg="#1e2a38", bd=5, relief="sunken", fg="white")
Input.grid(row=1, column=0, pady=(0, 12))
def configSelecionar():
    global textoArquivo
    arquivo = filedialog.askopenfilename(title="Selecione um arquivo")
    print("Arquivo selecionado:", arquivo)
    Input.delete(0, tk.END)
    textoArquivo = str(arquivo)
    Input.insert(0, textoArquivo)
def configConfirmar():
    Input.config(disabledforeground="#2ecc71", state="disabled", disabledbackground="#1e2a38")
# Texto para ser digitado
botaoArquivo = tk.Button(frameSelecaoArquivo, text="Selecionar", command=configSelecionar, bg="#1e2a38", fg="white", relief="groove", bd=3, width=12)
botaoArquivo.grid(row=2, column=0, padx=(0, 86))
# Inicia a digitação

botaoConfirmar = tk.Button(frameSelecaoArquivo, text="Enviar", command=configConfirmar, bg="#1e2a38", fg="white", relief="groove", bd=3, width=10)
botaoConfirmar.grid(row=2, column=0, padx=(99, 0))

tela.mainloop()