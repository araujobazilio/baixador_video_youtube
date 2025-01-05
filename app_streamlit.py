import os
import streamlit as st
from pytube import YouTube
import requests

def baixar_video(url):
    """
    Baixa o vídeo do YouTube usando pytube com tratamento de erros
    """
    try:
        # Criar pasta de downloads temporários
        pasta_temp = os.path.join(os.getcwd(), 'downloads_temp')
        os.makedirs(pasta_temp, exist_ok=True)

        # Criar barra de progresso
        barra_progresso = st.progress(0)

        # Função de progresso personalizada
        def on_progress(stream, chunk, bytes_remaining):
            total_size = stream.filesize
            bytes_downloaded = total_size - bytes_remaining
            percentage_of_completion = bytes_downloaded / total_size
            barra_progresso.progress(min(int(percentage_of_completion * 100), 100))

        # Modificar URL de Shorts para vídeo normal
        if 'shorts/' in url:
            url = url.replace('shorts/', 'watch?v=')

        # Criar objeto YouTube
        yt = YouTube(url, on_progress_callback=on_progress)

        # Selecionar stream de maior resolução
        stream = yt.streams.get_highest_resolution()

        # Caminho completo para o arquivo
        caminho_arquivo = os.path.join(pasta_temp, f"{yt.title}.mp4")

        # Baixar o vídeo
        stream.download(output_path=pasta_temp, filename=f"{yt.title}.mp4")

        # Completar barra de progresso
        barra_progresso.progress(100)

        return caminho_arquivo, yt.title
    
    except Exception as e:
        st.error(f"Erro ao baixar o vídeo: {e}")
        return None, None

def main():
    # Configuração da página
    st.set_page_config(page_title="Baixador de Vídeos do YouTube", page_icon="📥")
    
    # Título do aplicativo
    st.title("🎥 Baixador de Vídeos do YouTube")
    
    # Input para URL do vídeo
    url_video = st.text_input("Cole a URL do vídeo do YouTube")
    
    # Botão de download
    if st.button("Baixar Vídeo"):
        if url_video:
            # Limpar mensagens anteriores
            st.empty()
            
            # Iniciar download
            st.info("Iniciando download...")
            caminho_arquivo, titulo_video = baixar_video(url_video)
            
            # Se o download for bem-sucedido
            if caminho_arquivo:
                # Botão para baixar para pasta de downloads
                with open(caminho_arquivo, 'rb') as arquivo:
                    st.success(f"Vídeo '{titulo_video}' baixado com sucesso!")
                    st.download_button(
                        label="Salvar na Pasta Downloads",
                        data=arquivo,
                        file_name=os.path.basename(caminho_arquivo),
                        mime="video/mp4"
                    )
        else:
            st.warning("Por favor, insira uma URL do YouTube")

if __name__ == "__main__":
    main()
