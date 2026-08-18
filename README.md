# Cadastro de Produtos — Minicurso DevOps

Sisteminha simples de cadastro de produtos via terminal, feito em Python com banco de dados MySQL rodando no Azure. Projeto base do minicurso de DevOps, usado para praticar Git/GitHub, Cloud e conceitos de IaC.

## O que o projeto faz

Um CRUD bem enxuto, com apenas duas operações:
- **Cadastrar produto**: salva um nome e um valor no banco de dados.
- **Visualizar produtos**: lista todos os produtos já cadastrados.

## Pré-requisitos

Antes de começar, você vai precisar de:

- [Python 3.10+](https://www.python.org/downloads/) instalado na máquina
- Uma conta no [Azure](https://azure.microsoft.com/free/) (recomendado: [Azure for Students](https://azure.microsoft.com/free/students/), não precisa de cartão de crédito)
- Um servidor **Azure Database for MySQL – Flexible Server** já criado, com um banco de dados dentro dele
- [Git](https://git-scm.com/) instalado
- [VS Code](https://code.visualstudio.com/) (recomendado, mas qualquer editor funciona)

## Estrutura do projeto

```
minicurso-devops-app/
├── config.py
├── main.py
├── .env.example
└── .gitignore
```

## Como configurar

### 1. Fork e clone

Dê fork neste repositório pelo GitHub e depois clone a sua cópia:

```bash
git clone https://github.com/seu-usuario/nome-do-repo.git](https://github.com/renanolv7/project-devops-minicurso.git
cd nome-do-repo
```

### 2. Instalar as dependências

```bash
python -m pip install mysql-connector-python python-dotenv
```

### 3. Configurar a conexão com o banco (.env)

Copie o arquivo de exemplo e renomeie:

```bash
cp .env.example .env
```

Abra o `.env` e preencha com os dados do **seu** servidor Azure (você anota esses dados na hora que cria o servidor no portal):

```
DB_HOST=seu-servidor.mysql.database.azure.com
DB_USER=seu_usuario_admin
DB_PASSWORD=sua_senha
DB_NAME=nome_do_seu_banco
```

> ⚠️ O arquivo `.env` nunca deve ser enviado ao GitHub — ele já está listado no `.gitignore` para isso.

### 4. Liberar seu IP no firewall do Azure

No portal do Azure, dentro do seu servidor MySQL → **Networking** → **Firewall rules** → **Add current client IP address** → **Save**. Sem esse passo, a conexão é recusada mesmo com usuário e senha corretos.


### 5. Executar o projeto

```bash
python main.py
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
| `ModuleNotFoundError: No module named 'mysql'` | Rode `python -m pip install mysql-connector-python` usando o mesmo Python configurado no seu editor |
| `Unknown database 'xxx'` | O nome em `DB_NAME` no `.env` não bate com o banco criado no Azure, ou o banco ainda não existe — confira o nome ou crie o banco pelo portal |
| `Can't connect to MySQL server` | Seu IP não está liberado no firewall do Azure — veja o passo 4 |
| Menu não aparece / erro ao importar | Confira se está rodando `python main.py` de dentro da pasta do projeto, e se o `.env` está no mesmo lugar |

## Segurança

- **Nunca** commite o arquivo `.env` — ele contém a senha do banco.
- Use sempre o `.env.example` como referência de quais variáveis preencher, sem valores reais.
- Se a senha do banco vazar acidentalmente (ex: print de tela, mensagem, commit por engano), troque-a imediatamente no portal do Azure.

## Sobre

Projeto desenvolvido como material de apoio para o minicurso de DevOps do Scitech.
