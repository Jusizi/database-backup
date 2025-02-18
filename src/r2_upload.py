import os
import boto3
from datetime import datetime

def upload_to_r2(file_path, db_config):
    print(f"Iniciando o upload para o R2: {file_path}\n")
    
    # Criação de uma pasta para o dia do backup (formato: YYYY/MM/DD)
    today = datetime.now().strftime("%Y/%m/%d")
    object_name = os.path.basename(file_path)  # Nome do arquivo original
    object_path = f"{today}/{object_name}"  # Caminho completo com a data
    
    session = boto3.session.Session()
    s3 = session.client(
        service_name="s3",
        aws_access_key_id=db_config["R2_ACCESS_KEY"],
        aws_secret_access_key=db_config["R2_SECRET_KEY"],
        endpoint_url=db_config["R2_ENDPOINT"]
    )
    
    bucket_name = db_config["R2_BUCKET"]
    
    try:
        print(f"Enviando o arquivo {object_name} para o R2 na pasta {today}...\n")
        print(f"Bucket: {bucket_name}, Caminho do objeto: {object_path}\n")

        s3.upload_file(file_path, bucket_name, object_path)
        print(f"Backup {object_name} enviado para o R2 com sucesso.\n")
        
        # Remove o arquivo local após o upload
        os.remove(file_path)
    except Exception as e:
        print(f"Erro ao enviar para o R2:\n{e}\n")
