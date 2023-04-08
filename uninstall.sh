#!/usr/bin/env bash

# Define o destino do arquivo
destino="/usr/local/bin/abntbibcheck"

# Verifica se o arquivo existe no destino
if [ -f "$destino" ]; then
    # Remove o arquivo executável do destino
    sudo rm "$destino"
    
    # Verifica se o arquivo foi removido corretamente
    if [ ! -f "$destino" ]; then
        echo "abntbibcheck desinstalado com sucesso."
    else
        echo "Erro: a desinstalação do abntbibcheck falhou."
    fi
else
    echo "abntbibcheck não está instalado."
fi
