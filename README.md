# YouTube Video Downloader

## Descrição
Este script permite baixar vídeos do YouTube de forma simples e rápida, com suporte para download de vídeos únicos ou múltiplos.

## Funcionalidades
- Baixar vídeos individuais do YouTube
- Baixar múltiplos vídeos em uma única sessão
- Salva vídeos em uma pasta personalizada
- Tratamento de erros para URLs inválidas ou vídeos indisponíveis

## Dependências
- Python 3.7+
- yt-dlp
- Streamlit

## Instalação
1. Clone o repositório
2. Crie um ambiente virtual (opcional, mas recomendado)
3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Uso
Execute o script e siga as instruções no menu:
```bash
python baixar_video.py
```

### Opções
1. Baixar um único vídeo
2. Baixar múltiplos vídeos
3. Sair do programa

## Versões
- Script CLI: `baixar_video.py`
- Aplicativo Web: `app_streamlit.py`

## Executando o Aplicativo Streamlit
```bash
streamlit run app_streamlit.py
```

### Recursos
- Suporta download de vídeos completos, Shorts e outros formatos do YouTube
- Contorna restrições de download
- Barra de progresso em tempo real
- Interface simples e intuitiva

## Observações
- Os vídeos serão salvos na pasta `videos_baixados` por padrão
- Insira URLs completas do YouTube
- Digite 'done' para finalizar o download de múltiplos vídeos

## Aviso Legal
Respeite os direitos autorais e os termos de serviço do YouTube ao baixar vídeos.
