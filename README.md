# PostgreSQL Homelab + Python

Projeto desenvolvido para praticar a configuração de um banco de dados PostgreSQL em um ambiente de Homelab, permitindo o acesso remoto através da rede local e a integração com Python para execução de consultas SQL.

## 📌 Sobre o projeto

Neste projeto, configurei um servidor PostgreSQL dentro do meu Homelab e realizei a conexão com um notebook conectado à mesma rede local.

Após configurar o acesso remoto ao banco de dados, utilizei Python para estabelecer a conexão com o PostgreSQL e executar consultas diretamente através do código.

O objetivo principal foi compreender de forma prática como funciona a comunicação entre aplicações, redes e bancos de dados em um ambiente semelhante ao utilizado em aplicações reais.

## 🛠️ Tecnologias utilizadas

- PostgreSQL
- Python
- SQL
- Biblioteca `psycopg2`
- Rede local
- Homelab

## 🏗️ Arquitetura do projeto

O ambiente funciona de forma semelhante ao seguinte fluxo:

```text
┌──────────────────────┐
│       Homelab        │
│                      │
│  PostgreSQL Server   │
│      Porta 5432      │
└──────────┬───────────┘
           │
           │ Rede Local
           │
┌──────────▼───────────┐
│       Notebook       │
│                      │
│   Python + SQL       │
│      psycopg2        │
└──────────────────────┘
```

O PostgreSQL é executado no servidor do Homelab, enquanto o notebook realiza a conexão através do endereço IP do servidor na rede local.

## 🚀 Funcionalidades

O projeto permite:

- Conectar um computador remoto ao PostgreSQL através da rede local
- Criar conexão com o banco utilizando Python
- Executar consultas SQL pelo Python
- Recuperar dados armazenados no PostgreSQL
- Testar comunicação entre diferentes dispositivos da rede
- Praticar conceitos básicos de administração de banco de dados

## 🐍 Conexão com Python

Exemplo básico de conexão utilizando `psycopg2`:

```python
import psycopg2

conexao = psycopg2.connect(
    host="IP_DO_SERVIDOR",
    database="NOME_DO_BANCO",
    user="USUARIO",
    password="SENHA",
    port="5432"
)

cursor = conexao.cursor()

cursor.execute("SELECT * FROM tabela;")

dados = cursor.fetchall()

for linha in dados:
    print(linha)

cursor.close()
conexao.close()
```

> Por segurança, credenciais reais do banco de dados não devem ser armazenadas diretamente no código ou enviadas para o GitHub.

## 🔐 Boas práticas de segurança

Em projetos reais, o recomendado é armazenar informações sensíveis em variáveis de ambiente.

Exemplo:

```env
DB_HOST=192.168.0.100
DB_NAME=meubanco
DB_USER=usuario
DB_PASSWORD=senha
DB_PORT=5432
```

No Python, essas informações podem ser carregadas utilizando bibliotecas como `python-dotenv`.

Exemplo:

```python
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conexao = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT")
)
```

## ⚙️ Configuração do PostgreSQL

Para permitir o acesso através da rede local, foi necessário configurar o PostgreSQL para aceitar conexões externas.

Entre as principais configurações estão:

```text
postgresql.conf
```

Configurando o PostgreSQL para escutar conexões externas:

```conf
listen_addresses = '*'
```

E no arquivo:

```text
pg_hba.conf
```

É necessário autorizar o acesso da rede local.

Exemplo:

```conf
host    all    all    192.168.0.0/24    scram-sha-256
```

> As configurações podem variar de acordo com a rede e com o sistema operacional utilizado.

## 📂 Estrutura sugerida

```text
postgresql-homelab-python/
│
├── src/
│   ├── conexao.py
│   └── consultas.py
│
├── sql/
│   └── consultas.sql
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/postgresql-homelab-python.git
```

Entre na pasta:

```bash
cd postgresql-homelab-python
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install psycopg2-binary python-dotenv
```

Ou:

```bash
pip install -r requirements.txt
```

## 📄 requirements.txt

```text
psycopg2-binary
python-dotenv
```

## 🚫 .gitignore

É recomendado adicionar ao `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

Isso evita o envio de informações sensíveis e arquivos desnecessários para o repositório.

## 📚 Conhecimentos praticados

Durante o desenvolvimento deste projeto, pratiquei conceitos relacionados a:

- PostgreSQL
- SQL
- Python
- Conexão Python com banco de dados
- Cliente e servidor
- Redes locais
- Endereçamento IP
- Administração básica de banco de dados
- Acesso remoto
- Variáveis de ambiente
- Segurança de credenciais

## 🎯 Objetivo

Este projeto faz parte dos meus estudos em Ciência de Dados e tem como objetivo desenvolver experiência prática com bancos de dados, Python e infraestrutura.

A proposta foi ir além da execução de consultas SQL localmente, construindo um ambiente no qual o banco de dados é executado em outro dispositivo e acessado através da rede.

## 🔮 Próximos passos

Como evolução do projeto, pretendo implementar:

- Operações CRUD completas
- Criação de múltiplas tabelas relacionadas
- Joins e consultas mais avançadas
- Views no PostgreSQL
- Stored Procedures
- Integração com Pandas
- Análise dos dados utilizando Python
- Criação de uma API para acesso ao banco
- Dockerização do ambiente
- Backup automatizado do PostgreSQL

## 👨‍💻 Autor

**João Pedro Ramiro**

Estudante de Ciência de Dados.

- GitHub: https://github.com/joaopedroramiro321-source
- LinkedIn: https://www.linkedin.com/in/joaopedroramiro/
