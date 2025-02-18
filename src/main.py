import os
from dotenv import load_dotenv
from database_backup import DatabaseBackup
from discord_webhook import DiscordWebhook  # Importa a classe do Webhook do Discord

# Carrega variáveis do .env
load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")  # Webhook do Discord

DATABASE_NAME = os.getenv("DATABASE_NAME")  # Nome do banco de dados

# Instancia o webhook do Discord
discord = DiscordWebhook(DISCORD_WEBHOOK_URL)

if __name__ == "__main__":

    mensagem = "Iniciando backup para o banco de dados... :rocket:"
    print(mensagem)
    discord.send_message(mensagem)
    
    try: 
        
        db_backup = DatabaseBackup(DATABASE_NAME)
        db_backup.run()

        msg = f"Backup de **{DATABASE_NAME}** concluído com sucesso. :white_check_mark:"
        print(msg)
        discord.send_message(msg)  # Notifica conclusão do backup
    
    except Exception as e:
    
        msg = f"Erro ao realizar backup de **{DATABASE_NAME}** :x: :\n {e}"
        print(msg)
        discord.send_message(msg)