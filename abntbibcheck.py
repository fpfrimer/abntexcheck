#!/usr/bin/env python3

"""
abntbibcheck.py

Descrição:
    Este script verifica se as entradas de um arquivo BibTeX estão em conformidade
    com as normas da ABNT (Associação Brasileira de Normas Técnicas) e aponta
    possíveis melhorias ou correções a serem feitas.

Autor:
    Felipe Walter Dafico Pfrimer <https://github.com/fpfrimer/abntexcheck>

Data de criação:
    07 de abril de 2023

Última atualização:
    07 de abril de 2023

Licença:
    MIT License
"""

import sys
from pybtex.database.input import bibtex
import re
import argparse

# Cores ANSI
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"

def verifica_coerencia_abnt(entry):
    """
    O método verifica a coerência de uma entrada BibTeX com as normas da ABNT, identificando
    campos obrigatórios faltantes, campos recomendados faltantes, possíveis sub-títulos
    incluídos no campo de título e possíveis designações de parentesco no campo de autor.
    
    Parâmetros:
        entry (pybtex.database.Entry): Entrada BibTeX a ser verificada.
        
    Retorna:
        tuple: Uma tupla contendo quatro listas:
            - campos_faltando: Lista de campos obrigatórios faltantes.
            - campos_recomendados_faltando: Lista de campos recomendados faltantes.
            - possivel_subtitulo: Lista de campos onde possíveis sub-títulos foram identificados.
            - possivel_parentesco: Lista de campos onde possíveis designações de parentesco foram identificadas.
    """

    # ...
    # Dicionários com campos necessários e recomendados para cada tipo de entrada
    # de acordo com a ABNT. Estes dicionários podem ser modificados para refletir
    # as necessidades específicas do usuário ou atualizações nas normas da ABNT.
    necessarios = {
        'article': ['author', 'title', 'journal', 'year','address'],
        'book': ['author', 'title', 'publisher', 'year'],
        'booklet': ['title'],
        'inbook': ['author', 'title', 'publisher', 'year', 'pages'],
        'incollection': ['author', 'title', 'booktitle', 'publisher', 'year'],
        'inproceedings': ['author', 'title', 'booktitle', 'year'],
        'manual': ['title'],
        'mastersthesis': ['author', 'title', 'school', 'year'],
        'phdthesis': ['author', 'title', 'school', 'year'],
        'proceedings': ['title', 'year'],
        'techreport': ['author', 'title', 'institution', 'year'],
        'unpublished': ['author', 'title', 'note'],
    }

    recomendados = {
        'article': ['volume', 'number', 'pages', 'month', 'doi', 'url', 'issn'],
        'book': ['volume', 'series', 'address', 'edition', 'month', 'doi', 'url', 'isbn'],
        'booklet': ['author', 'howpublished', 'address', 'month', 'year', 'note', 'url'],
        'inbook': ['volume', 'series', 'type', 'address', 'edition', 'month', 'doi', 'url', 'isbn'],
        'incollection': ['editor', 'volume', 'series', 'type', 'address', 'edition', 'month', 'pages', 'doi', 'url', 'isbn'],
        'inproceedings': ['editor', 'volume', 'series', 'pages', 'address', 'month', 'organization', 'publisher', 'doi', 'url', 'isbn'],
        'manual': ['author', 'organization', 'address', 'edition', 'month', 'year', 'note', 'url'],
        'mastersthesis': ['address', 'month', 'note', 'url'],
        'phdthesis': ['address', 'month', 'note', 'url'],
        'proceedings': ['editor', 'volume', 'series', 'address', 'month', 'organization', 'publisher', 'doi', 'url', 'isbn'],
        'techreport': ['type', 'number', 'address', 'month', 'doi', 'url', 'issn'],
        'unpublished': ['month', 'year', 'url'],
    }

    # Lista de designações de parentesco
    parentescos = ['Filho', 'Neto', 'Júnior', 'Sobrinho', 'Bisneto', 'Trineto', 'Tataraneto', 'Terceiro', 'Quarto']
    pattern = r'\b(?:' + '|'.join(parentescos) + r')\b'

    tipo = entry.type.lower()
    campos_faltando = []
    campos_recomendados_faltando = []
    possivel_subtitulo = []
    possivel_parentesco = []

    if tipo in necessarios:
        campos = necessarios[tipo]
        for campo in campos:
            # print(entry.persons['author'][1])
            if campo == 'author':
                if 'author' not in entry.persons:                    
                    campos_faltando.append(campo)
            elif campo == 'title':                
                if re.search("[:–]", entry.fields['title']):
                    possivel_subtitulo.append(campo)
                if re.search(pattern, str(entry.persons['author'])):
                    possivel_parentesco.append(campo)
            else:
                if campo not in entry.fields:
                    campos_faltando.append(campo)

        campos_recomendados = recomendados.get(tipo, [])
        for campo in campos_recomendados:
            if campo not in entry.fields:
                campos_recomendados_faltando.append(campo)

    else:
        return campos_faltando, campos_recomendados_faltando, possivel_subtitulo, possivel_parentesco

    return campos_faltando, campos_recomendados_faltando, possivel_subtitulo, possivel_parentesco

def main(bibtex_file, color_output):
    """
    A função principal do programa que analisa um arquivo BibTeX e verifica a coerência
    de suas entradas em relação às normas ABNT. Para cada entrada, a função verifica
    se os campos necessários e recomendados estão presentes e se há possíveis problemas
    com subtítulos ou designações de parentesco nos nomes dos autores. As informações
    sobre as entradas incoerentes e recomendações são exibidas no terminal.

    :param bibtex_file: O caminho do arquivo BibTeX a ser analisado.
    """

    if not color_output:
        global RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, RESET
        RED = GREEN = YELLOW = BLUE = MAGENTA = CYAN = RESET = ""

    # Cria um objeto Parser da biblioteca pybtex.database.input.bibtex. 
    # Este objeto é usado para analisar arquivos BibTeX e carregar suas 
    # informações em um objeto de dados específico da biblioteca.
    parser = bibtex.Parser()
    try:
        bib_data = parser.parse_file(bibtex_file)
    except Exception as e:
        print(f"\nHouston, nós temos um problema! Erro ao analisar o arquivo BibTeX:\n\t {e}\n")
        sys.exit(1)

    # Percorre todas as entradas do arquivo bib
    for key, entry in bib_data.entries.items():
        campos_faltando, campos_recomendados_faltando, possivel_subtitulo, possivel_parentesco = verifica_coerencia_abnt(entry)
        if campos_faltando:
            print(f'Entrada {RED}{key}{RESET} não está coerente com a ABNT. Campos faltando: {RED}{", ".join(campos_faltando)}{RESET}')
        if campos_recomendados_faltando:
            print(f'Entrada {GREEN}{key}{RESET}: Recomendamos a inclusão dos seguintes campos: {GREEN}{", ".join(campos_recomendados_faltando)}{RESET}')
        if possivel_subtitulo:
            print(f'Entrada {YELLOW}{key}{RESET}: Subtítulo possivelmente incluído no campo: {YELLOW}{", ".join(possivel_subtitulo)}{RESET}')
        if possivel_parentesco:
            print(f'Entrada {YELLOW}{key}{RESET}: Verificar nome que é possível parentesco (Neto, Filho, Júnior, etc.): {YELLOW}{", ".join(possivel_parentesco)}{RESET}')

# Executa a main
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verifica a coerência de um arquivo BibTeX em relação às normas ABNT.")
    parser.add_argument("bibtex_file", help="O caminho do arquivo BibTeX a ser analisado.")
    parser.add_argument("-c", "--color", action="store_true", help="Ativa a saída colorida (desativado por padrão).")

    args = parser.parse_args()

    main(args.bibtex_file, args.color)
