# Equivalencia-Logica-APP

## Criação do Ambiente

01. No diretório origem do projeto crie um ambiente virtual do python:
    
        python -m venv venv

02. Ative o ambiente virtual:
    
        ./venv/Scripts/activate

03. Instale as bibliotecas que são necessárias pelo arquivo requirements.txt:

        pip install -r requirements.txt

## Utilizando o Projeto

01. Com o ambiente configurado, inicie o projeto Flask:

        flask run

02. Consulte o site em:

        localhost:5000/

## Utilizando Docker

01. No diretório de origem abra o terminal e builde a aplicação:

        
        docker build -t grupozada/logical-app .

02. Após o build da imagem continue no terminal e digite:

        docker container run --name logical-app -p 5000:5000 grupozada/logical-app
