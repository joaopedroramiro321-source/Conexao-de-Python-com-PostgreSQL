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

```
