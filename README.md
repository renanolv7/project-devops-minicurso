# Minicurso DevOps — Cadastro de Produtos 

Sistema simples de cadastro de produtos via terminal, feito em Python com banco de dados MySQL rodando no Azure. Projeto base do minicurso de DevOps, usado para praticar Git/GitHub, Cloud, Conceitos de conexão entre aplicação e servidor.

## O que o projeto faz

Um CRUD bem enxuto, com apenas duas operações:
- **Cadastrar produto**: salva um nome e um valor no banco de dados.
- **Visualizar produtos**: lista todos os produtos já cadastrados.

## Pré-requisitos

Antes de começar, você vai precisar de:

- Uma conta no [Azure](https://azure.microsoft.com/free/) (recomendado: [Azure for Students](https://azure.microsoft.com/free/students/), não precisa de cartão de crédito)
- [Python 3.10+](https://www.python.org/downloads/) instalado na máquina
- pyodbc instalado na máquina (ODBC Driver 18 for SQL Server).
- [Git](https://git-scm.com/) instalado
- [VS Code](https://code.visualstudio.com/) (recomendado, mas qualquer editor funciona)


## Estrutura do projeto

```
project-devops-minicurso/
├── src/
│   ├── database.py
│   ├── main.py
│   └── sql/                     
│       └── criar_tebela.sql
├── tests/
├── .env
├── .env.example
├── .gitignore
└── README.md
```

## Como configurar

### 1. Fork/Clone

Dê fork neste repositório pelo GitHub e depois clone a sua cópia:

```bash
git clone https://github.com/seu-usuario/nome-do-repo.git
cd nome-do-repo
```

### 2. Criar ambiente e instalar bibliotecas.

Criar ambiente:
```bash
python -m venv .venv
```

Ativar ambiente:
```bash
.venv\Scripts\activate.bat
```

#### Instalar todas as dependências necessárias

```bash
python -m pip install pyodbc python-dotenv
```

Desativar para sair do ambiente virtual:
```bash
deactivate
```

### 4. Configurar a conexão com o banco.

Há várias formas diferentes de conectar uma aplicação ao servidor do banco de dados. Seja ela por um SGBD, string de conexão no próprio código, extensões... 

#### Antes de prosseguir, encontrará a pasta (`sql`) com o arquivo (`setup_inicial_db.sql`), execute esse arquivo. O arquivo é responsável pela criação da tabela PRODUTOS e inserção de alguns produtos para teste.

Após o setup inicial, separamos duas formas diferentes possíveis de se a realizar a conexão ao banco de dados:

**4.1  Via aplicação Python (`.env`)**
 
É como o próprio programa se conecta para cadastrar e visualizar produtos. 

Copie o arquivo de exemplo e renomeie:
 
```bash
cp .env.example .env
```

Preencher o arquivo `.env`:
 
```
DB_HOST=seu-servidor.database.azure.com
DB_USER=seu_usuario_admin
DB_PASSWORD=sua_senha
DB_NAME=nome_do_seu_banco
```
 
Os dados acima são encontrados no seu servidor Azure (você anota esses dados na hora que cria o servidor no portal).
 
⚠️ O arquivo `.env` nunca deve ser enviado ao GitHub, ele já está listado no `.gitignore` para isso.

Em seguida rode o arquivo `main`:

```bash
python src/main.py
```
 
**4.2  Via extensão SQL Server no VS Code**
 
Forma visual, útil para criar tabelas e consultas. Instale a extensão **SQL server**, crie uma nova conexão com os mesmos dados do `.env` (host, usuário, senha, porta `1433`).
 
> ⚠️ A extensão não lê o `.env` automaticamente, você preenche os dados de novo, direto na interface.

Para executar comandos SQL através da extensão, crie um novo arquivo de Query, como na imagem abaixo:


Um exemplo de SQL:

```sql
CREATE TABLE produtos (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nome_produto VARCHAR(100) NOT NULL,
    valor DECIMAL(10,2) NOT NULL
);
```

### 5. Liberar seu IP no firewall do Azure

No portal do Azure, dentro do seu banco de dados SQL, acesse **Propriedades** → **Rede** → **Regras de Firewall** → **Adicionar o endereço IP do cliente atual** → **Salve**. Sem esse passo, a conexão é recusada mesmo com usuário e senha corretos.

Caso seja necessário, pesquise pelo IP da sua máquina e preencha manualmente, de tempos em tempos esse endereço pode ser atualizado e não aparecer da forma correta na hora de 'Adicionar o endereço IP do cliente atual'.

### Falhou? Confira nessa ordem: host → porta → usuário → senha → firewall → internet → status do servidor no Azure.

### 6. Executar o projeto

```bash
python src/main.py
```

## Como usar

Ao rodar, o programa mostra um menu:

```
========================================
   1 - Cadastrar produto
   2 - Visualizar produtos
   3 - Sair
========================================
```

- Digite **1** para cadastrar um novo produto (o programa vai pedir nome e valor).
- Digite **2** para ver a lista de produtos já cadastrados.
- Digite **3** para encerrar o programa.

## Solução de problemas comuns

| Erro | O que fazer |
|---|---|
| `Unknown database 'xxx'` | O nome em `DB_NAME` no `.env` não bate com o banco criado no Azure, ou o banco ainda não existe, confira o nome ou crie o banco pelo portal |
| `Can't connect to SQL server` | Seu IP não está liberado no firewall do Azure, veja o passo 4 |
| `Authentication plugin 'caching_sha2_password' is not supported` | O erro corre porque o MySQL 8+ usa por padrão o plugin de autenticação caching_sha2_password, mas a biblioteca que você está usando no Python está desatualizada ou não reconhece esse método nativamente. Instalar a biblioteca correta. |
| Menu não aparece / erro ao importar | Confira se está rodando `python src/main.py` de dentro da pasta do projeto, e se o `.env` está no mesmo lugar |

## Segurança

- **Nunca** commite o arquivo `.env`, ele contém a senha do banco.
- Use sempre o `.env.example` como referência de quais variáveis preencher, sem valores reais.
- Se a senha do banco vazar acidentalmente (ex: print de tela, mensagem, commit por engano), troque-a imediatamente no portal do Azure.

## Sobre

Projeto desenvolvido pela equipe de instrutores do curso como material de apoio para o minicurso de DevOps do Scitech.


