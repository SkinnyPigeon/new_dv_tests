from dotenv import load_dotenv
import subprocess
import os

def get_password_and_port():
    project_folder = subprocess.check_output(
    "pwd", shell=True).decode("utf-8").rstrip()
    load_dotenv(os.path.join(project_folder, '.env'))
    PORT = os.getenv('PGPORT')
    PASSWORD = os.getenv('PGPASSWORD')
    if PORT == None:
        PASSWORD = os.environ.get('PGPASSWORD')
        PORT = os.environ.get('PGPORT')
    return PASSWORD, PORT

PASSWORD, PORT = get_password_and_port()