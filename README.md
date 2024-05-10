# Sistema em Django com App Core

Este é um sistema web desenvolvido em Django, um framework web popular para Python. O sistema inclui um aplicativo principal chamado "Core", que possui três templates principais:

1. **Contato**: Este template inclui um formulário para envio de e-mails de contato.

2. **Produto**: Este template inclui um formulário para cadastro de produtos em um banco de dados MySQL.

3. **Index**: Este é o template principal que lista os produtos cadastrados no banco de dados.

## Configuração do Banco de Dados

Este sistema utiliza o banco de dados MySQL para armazenar informações sobre os produtos cadastrados. Certifique-se de configurar corretamente as credenciais do banco de dados no arquivo `settings.py` do projeto Django.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_banco_de_dados',
        'USER': 'usuario_do_banco',
        'PASSWORD': 'senha_do_banco',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Substitua `'nome_do_banco_de_dados'`, `'usuario_do_banco'` e `'senha_do_banco'` pelos detalhes de conexão do seu banco de dados MySQL.

## Como executar o sistema

Para executar este sistema em seu ambiente local, siga estas etapas:

1. Clone o repositório para o seu computador:

```
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

2. Navegue até o diretório do projeto:

```
cd nome-do-repositorio
```

3. Instale as dependências do Python listadas no arquivo `requirements.txt`:

```
pip install -r requirements.txt
```

4. Execute as migrações para criar as tabelas do banco de dados:

```
python manage.py migrate
```

5. Inicie o servidor de desenvolvimento:

```
python manage.py runserver
```

6. Acesse o sistema em seu navegador web em `http://localhost:8000/`.

## Contribuindo

Se você deseja contribuir com este projeto, fique à vontade para enviar pull requests ou abrir issues no repositório do GitHub.

## Autores

- Renato Pasklan

## Licença

Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT) - veja o arquivo `LICENSE` para mais detalhes.

--- 

Este README fornece uma visão geral do sistema em Django, incluindo sua estrutura, configuração do banco de dados, instruções de execução e informações sobre contribuições e licenciamento. Sinta-se à vontade para personalizá-lo conforme necessário para o seu projeto específico.
