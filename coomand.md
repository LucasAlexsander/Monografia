Instala o ambiente virtual: python3  -m venv env
Entrada no ambiente virtual:  source env/bin/activate
Instalar o django: pip3 install django
Lista os pacotes instalados: pip3 list
Comando freeze: pip3 freeze
Criar o arquivo de requiriments: pip3 freeze > requirements.txt
Lista o conteudo do arquivo: cat requirements.txt
Instala as dependencias do requiriments: pip3 -r install requiriments.txt 
Criar o projeto django: django-admin startproject monografias .
Roda o django: ./manage.py runserver 0.0.0:8000

Arquivo settings.py: 
    Alterar o ALLOWED_HOSTS = ['*'] para outras maquinas conseguirem acessar.
    LANGUAGE_CODE = 'pt-br'
    TIME_ZONE = 'America/Sao_Paulo'

Criar a aplicação home: ./manage.py startapp home 
Registrar a aplicação home em: INSTALLED_APPS no arquivo settings.py
Criar a urls.py dentro da aplicação home
Adicionar o chamado da rota home na urls.py:  path('', include('home.urls')),

criar a pasta template dentro da pasta raiz do projeto, adicionar na settings.py "template" dirs "templates" 
    Criar dentro da template da pasta base do projeto: base.html e menu.html

Bootstrap - framework para "ajustar" a pagina

Para rodar: ./manage.py runserver