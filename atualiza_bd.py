import streamlit as st
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import tempfile

def authenticate():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()  # Autenticação via navegador
    return GoogleDrive(gauth)

def list_files_in_folder(drive, folder_id):
    query = f"'{folder_id}' in parents and trashed=false"
    file_list = drive.ListFile({'q': query}).GetList()
    return {file['title']: file['id'] for file in file_list}

def download_file(drive, file_id):
    file = drive.CreateFile({'id': file_id})
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    file.GetContentFile(temp_file.name)
    return temp_file.name

st.title("Google Drive File Viewer")

drive = authenticate()

folder_id = st.text_input("Digite o ID da pasta do Google Drive:")

if folder_id:
    files = list_files_in_folder(drive, folder_id)
    if files:
        selected_file = st.selectbox("Selecione um arquivo:", list(files.keys()))
        
        if selected_file:
            file_path = download_file(drive, files[selected_file])
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            st.text_area("Conteúdo do arquivo:", content, height=300)
    else:
        st.write("Nenhum arquivo encontrado na pasta.")
