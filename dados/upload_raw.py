import boto3
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

BUCKET = "sprint02-datalake-wellington"

s3 = boto3.client(
    "s3",
    region_name=os.getenv("AWS_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)

def upload_arquivo(caminho_local: str, nome_arquivo: str):
    # Organiza por data automaticamente
    hoje = datetime.now().strftime("%Y/%m/%d")
    chave_s3 = f"raw/{hoje}/{nome_arquivo}"

    s3.upload_file(caminho_local, BUCKET, chave_s3)
    print(f"Upload realizado: s3://{BUCKET}/{chave_s3}")

if __name__ == "__main__":
    upload_arquivo("dados/temperatura.csv", "temperatura.csv")