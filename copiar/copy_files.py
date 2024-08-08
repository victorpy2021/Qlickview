import paramiko
import os
from pathlib import Path

def sftp_transfer(host, port, username, password, remote_path, local_path):
    try:
        # Crear una conexión SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port=port, username=username, password=password)

        # Crear una sesión SFTP
        sftp = ssh.open_sftp()

        # Verificar si el directorio remoto existe
        try:
            sftp.stat(remote_path)
        except FileNotFoundError:
            print(f"El directorio remoto {remote_path} no existe.")
            return

        # Descargar archivos del directorio remoto
        for item in sftp.listdir(remote_path):
            remote_file = os.path.join(remote_path, item)
            local_file = os.path.join(local_path, item)

            if sftp.stat(remote_file).st_mode & 0o40000:  # Directorio
                Path(local_file).mkdir(parents=True, exist_ok=True)
                sftp_transfer(host, port, username, password, remote_file, local_file)
            else:  # Archivo
                sftp.get(remote_file, local_file)
                print(f"Archivo {item} copiado exitosamente.")

        # Cerrar la sesión SFTP y SSH
        sftp.close()
        ssh.close()
        print("Transferencia completada con éxito.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Configura los parámetros aquí
    host = "192.168.88.74"  # IP del servidor Azure
    port = 22
    username = "usuario"  # Nombre de usuario del servidor Azure
    password = "contraseña"  # Contraseña del servidor Azure
    remote_path = "/ruta/remota/a/copiar"  # Ruta del directorio remoto en Azure
    local_path = "C:/ruta/local/destino"  # Ruta local en el servidor físico

    sftp_transfer(host, port, username, password, remote_path, local_path)
