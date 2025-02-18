import os
import subprocess
from datetime import datetime

def create_backup(db_config):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = "backups"  # Diretório para armazenar os backups
    os.makedirs(backup_dir, exist_ok=True)  # Cria o diretório se não existir
    
    # **Gerar backup diretamente no formato esperado**
    backup_file = os.path.join(backup_dir, f"backup_{db_config['DB_NAME']}_{timestamp}.dump")
    
    print(f"Iniciando dump do banco de dados {db_config['DB_NAME']} para {backup_file}...\n")

    dump_command = [
        "pg_dump",
        "-h", db_config["DB_HOST"],
        "-p", db_config["DB_PORT"],
        "-U", db_config["DB_USER"],
        "-d", db_config["DB_NAME"],
        "-F", "c",  # **Formato personalizado (binário)**
        "-f", backup_file
    ]
    
    env = os.environ.copy()
    env["PGPASSWORD"] = db_config["DB_PASSWORD"]
    
    try:
        subprocess.run(dump_command, env=env, check=True)
        print(f"Backup do banco de dados {db_config['DB_NAME']} concluído com sucesso: {backup_file}\n")
        return backup_file  # **Retorna o arquivo `.dump`**
    except subprocess.CalledProcessError as e:
        raise Exception(f"Erro ao criar backup: {e}\n")