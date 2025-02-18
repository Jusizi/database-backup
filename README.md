# Backup da Database para Cloudflare R2

Este projeto realiza o backup da database PostgreSQL e envia o arquivo para o R2 da Cloudflare.

## Estrutura do Projeto
```
/database-backup-to-r2
│── /backups --ignore
│── /src
│   │── backup.py
│   │── database_backup.py
│   │── discord_webhook.py
│   │── main.py
│   │── r2_upload.py
│── /.env --ignore
│── /.gitignore
│── /env_example
│── /README.md
│── /requirements.txt
```

## Pré-requisitos
- Python 3 instalado
- PostgreSQL instalado e configurado
- Conta Cloudflare R2 configurada
- Credenciais armazenadas no arquivo `.env`

## Configuração do `.env`
Crie um arquivo `.env` na raiz do projeto e adicione suas credenciais:
```
DB_HOST=XXXXXXXXX
DATABASE_NAME=XXXXXXXXXX
DB_PASSWORD=XXXXXXXXXX
DB_USER=XXXXXXXXXX
DB_PORT=XXXX

R2_BUCKET=XXXXXXXXXXXXXXX

R2_ESCRITA_TOKEN=XXXXXXXXXXXXXXXXXXXXXXX
R2_ESCRITA_ACCESS_KEY=XXXXXXXXXXXXXXXXXXXXXXX
R2_ESCRITA_SECRET_KEY=XXXXXXXXXXXXXXXXXXXXXXX
R2_ESCRITA_ENDPOINT=XXXXXXXXXXXXXXXXXXXXXX

DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/XXXXXXXXXXXXXXXXXXXXXXX/YYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
```

## Instalação
Dentro do diretório do projeto, execute:
```sh
pip install -r requirements.txt
```

## Como Executar
Para iniciar o backup e upload para o R2 execute:
```sh
python3 src/main.py
```

## Funcionamento
1. O script `backup.py` realiza o backup da database `minha_database` usando `pg_dump`.
2. O script `r2_upload.py` envia o backup para o R2 da Cloudflare.
3. O backup é removido localmente após o upload bem-sucedido.

## Autor
Desenvolvido por Matheus Maydana & GPJhonsom 🚀
