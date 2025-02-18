import os
from dotenv import load_dotenv
from backup import create_backup
from r2_upload import upload_to_r2

class DatabaseBackup:
    def __init__(self, db_name):
        self.db_name = db_name
        self.config = self.load_env()

    def load_env(self):
        print("Carregando variáveis de ambiente...\n")
        load_dotenv()
        return {
            "DB_NAME": self.db_name,
            "DB_USER": os.getenv("DB_USER"),
            "DB_PASSWORD": os.getenv("DB_PASSWORD"),
            "DB_HOST": os.getenv("DB_HOST", "localhost"),
            "DB_PORT": os.getenv("DB_PORT", "5432"),
            "R2_ACCESS_KEY": os.getenv("R2_ESCRITA_ACCESS_KEY"),
            "R2_SECRET_KEY": os.getenv("R2_ESCRITA_SECRET_KEY"),
            "R2_ENDPOINT": os.getenv("R2_ESCRITA_ENDPOINT"),
            "R2_BUCKET": os.getenv("R2_BUCKET"),
        }

    def create_backup(self):
        print(f"Criando backup para o banco de dados {self.db_name}...\n")
        return create_backup(self.config)

    def upload_to_r2(self, backup_file):
        if backup_file:
            print(f"Backup criado com sucesso: {backup_file}\n")
            upload_to_r2(backup_file, self.config)
        else:
            Exception("Erro ao criar backup. Backup não encontrado.\n")

    def run(self):
        backup_file = self.create_backup()
        self.upload_to_r2(backup_file)