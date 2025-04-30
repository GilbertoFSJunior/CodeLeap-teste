# Backend com FastAPI – Gerenciamento de Posts

## 📝 Sobre o projeto
Este backend foi desenvolvido usando **FastAPI** para gerenciar posts com operações CRUD (Criar, Ler, Atualizar, Excluir).  
Os testes automatizados foram implementados com **Pytest**.

## 📂 Estrutura de arquivos

📁 projeto_backend  ├── main.py          # Código principal do backend 
                     ├── test_main.py     # Testes automatizados 
                      ├── requirements.txt # Dependências do projeto ├── README.md        # Documentação



## 🚀 Como executar o backend
1. **Instalar dependências**  
   Certifique-se de ter Python instalado. Depois, instale os pacotes necessários:
   ```sh
   pip install fastapi uvicorn pydantic pytest httpx

## Rodar o Servidor
    uvicorn main:app --reload
    O servidor será iniciado e poderá ser acessado em http://127.0.0.1:8000.

## Como rodar os testes
    Execute o seguinte comando na pasta onde está test_main.py:
    pytest test_main.py

    
