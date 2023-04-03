#!/bin/bash

# Define o destino do arquivo
destino="/usr/local/bin/abntbibcheck"

# Move o arquivo executável para o destino
sudo cp abntbibcheck.py "$destino"

# Verifica se o arquivo foi copiado corretamente
if [ -f "$destino" ]; then
    echo "abntbibcheck instalado com sucesso."
else
    echo "Erro: a instalação do abntbibcheck falhou."
fi
