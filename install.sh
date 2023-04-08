#!/usr/bin/env bash

# Função para verificar se uma biblioteca Python está instalada
function check_python_library() {
    library_name=$1
    python3 -c "import $library_name" 2>/dev/null

    if [ $? -ne 0 ]; then
        echo "A biblioteca Python '$library_name' não está instalada. Por favor, instale-a usando 'pip install $library_name'."
        exit 1
    fi
}

# Verifica se as bibliotecas Python necessárias estão instaladas
check_python_library "pybtex"
check_python_library "re"

# Define o destino do arquivo
destino="/usr/local/bin/abntbibcheck"

# Verifica se o arquivo já existe e solicita confirmação do usuário
if [ -f "$destino" ]; then
    read -p "O arquivo $destino já existe. Deseja sobrescrevê-lo? (S/N) " resposta
    if [[ ! $resposta =~ ^[Ss]$ ]]; then
        echo "Instalação cancelada."
        exit 1
    fi
fi

# Move o arquivo executável para o destino
sudo cp abntbibcheck.py "$destino"

# Adiciona permissão de execução ao arquivo
sudo chmod +x "$destino"

# Verifica se o arquivo foi copiado corretamente
if [ -f "$destino" ]; then
    echo "abntbibcheck instalado com sucesso."
else
    echo "Erro: a instalação do abntbibcheck falhou."
fi
