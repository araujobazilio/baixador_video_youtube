import os
from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable

def baixar_video(url, pasta_destino=None):
    """
    Baixa um vídeo do YouTube com tratamento de erros.
    
    :param url: URL do vídeo do YouTube
    :param pasta_destino: Pasta onde o vídeo será salvo (opcional)
    :return: Caminho do arquivo baixado ou None se falhar
    """
    try:
        # Se nenhuma pasta for especificada, usa a pasta atual
        if pasta_destino is None:
            pasta_destino = os.path.join(os.getcwd(), 'videos_baixados')
        
        # Cria a pasta de destino se não existir
        os.makedirs(pasta_destino, exist_ok=True)
        
        # Cria objeto YouTube
        video = YouTube(url)
        
        # Seleciona a melhor resolução disponível
        stream = video.streams.get_highest_resolution()
        
        # Baixa o vídeo
        print(f"Baixando: {video.title}")
        caminho_arquivo = stream.download(output_path=pasta_destino)
        
        print(f"Vídeo baixado com sucesso: {video.title}")
        return caminho_arquivo
    
    except RegexMatchError:
        print("URL inválida. Verifique o link do YouTube.")
    except VideoUnavailable:
        print("Vídeo indisponível. Pode estar privado ou removido.")
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")
    
    return None

def baixar_multiplos_videos(urls, pasta_destino=None):
    """
    Baixa múltiplos vídeos do YouTube.
    
    :param urls: Lista de URLs dos vídeos
    :param pasta_destino: Pasta onde os vídeos serão salvos (opcional)
    :return: Lista de caminhos dos arquivos baixados
    """
    videos_baixados = []
    for url in urls:
        arquivo = baixar_video(url, pasta_destino)
        if arquivo:
            videos_baixados.append(arquivo)
    return videos_baixados

def main():
    # Exemplo de uso
    while True:
        print("\n--- Baixador de Vídeos do YouTube ---")
        print("1. Baixar um único vídeo")
        print("2. Baixar múltiplos vídeos")
        print("3. Sair")
        
        escolha = input("Escolha uma opção (1/2/3): ")
        
        if escolha == '1':
            url = input("Digite a URL do vídeo do YouTube: ")
            baixar_video(url)
        
        elif escolha == '2':
            urls = []
            while True:
                url = input("Digite a URL do vídeo (ou 'done' para concluir): ")
                if url.lower() == 'done':
                    break
                urls.append(url)
            
            baixar_multiplos_videos(urls)
        
        elif escolha == '3':
            print("Encerrando o programa...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
