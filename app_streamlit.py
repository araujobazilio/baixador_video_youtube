import os
import streamlit as st
import yt_dlp

def baixar_video(url):
    """
    Baixa o vídeo do YouTube usando yt-dlp
    """
    try:
        # Criar pasta de downloads temporários
        pasta_temp = os.path.join(os.getcwd(), 'downloads_temp')
        os.makedirs(pasta_temp, exist_ok=True)

        # Configurações do yt-dlp
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': os.path.join(pasta_temp, '%(title)s.%(ext)s'),
        }

        # Criar barra de progresso
        barra_progresso = st.progress(0)

        # Função para atualizar progresso
        def progress_hook(d):
            if d['status'] == 'downloading':
                p = d.get('downloaded_bytes', 0)
                t = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
                if t > 0:
                    progresso = int(p * 100 / t)
                    barra_progresso.progress(min(progresso, 100))
            
            if d['status'] == 'finished':
                barra_progresso.progress(100)

        # Adicionar hook de progresso
        ydl_opts['progress_hooks'] = [progress_hook]

        # Baixar vídeo
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extrair informações do vídeo
            info_dict = ydl.extract_info(url, download=True)
            
            # Preparar nome do arquivo
            arquivo = ydl.prepare_filename(info_dict)
            
            # Obter título do vídeo
            titulo = info_dict.get('title', 'video')

        return arquivo, titulo
    
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
