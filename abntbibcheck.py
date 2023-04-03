#!/usr/bin/env python3


import sys
from pybtex.database.input import bibtex
import re

# Cores ANSI
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"

def verifica_coerencia_abnt(entry):
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


    tipo = entry.type.lower()
    campos_faltando = []
    campos_recomendados_faltando = []
    possivel_subtitulo = []

    if tipo in necessarios:
        campos = necessarios[tipo]
        for campo in campos:
            if campo == 'author':
                if 'author' not in entry.persons:
                    campos_faltando.append(campo)
            elif campo == 'title':                
                if re.search("[:–]", entry.fields['title']):
                    possivel_subtitulo.append(campo)
            else:
                if campo not in entry.fields:
                    campos_faltando.append(campo)

        campos_recomendados = recomendados.get(tipo, [])
        for campo in campos_recomendados:
            if campo not in entry.fields:
                campos_recomendados_faltando.append(campo)

    else:
        return campos_faltando, campos_recomendados_faltando, possivel_subtitulo

    return campos_faltando, campos_recomendados_faltando, possivel_subtitulo

def main(bibtex_file):
    parser = bibtex.Parser()
    bib_data = parser.parse_file(bibtex_file)

    for key, entry in bib_data.entries.items():
        campos_faltando, campos_recomendados_faltando, possivel_subtitulo = verifica_coerencia_abnt(entry)
        if campos_faltando:
            print(f'Entrada {RED}{key}{RESET} não está coerente com a ABNT. Campos faltando: {RED}{", ".join(campos_faltando)}{RESET}')
        if campos_recomendados_faltando:
            print(f'Entrada {GREEN}{key}{RESET}: Recomendamos a inclusão dos seguintes campos: {GREEN}{", ".join(campos_recomendados_faltando)}{RESET}')
        if possivel_subtitulo:
            print(f'Entrada {YELLOW}{key}{RESET}: Subtítulo possivelmente incluído no campo: {YELLOW}{", ".join(possivel_subtitulo)}{RESET}')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python verificador_abnt.py <arquivo_bibtex>")
        sys.exit(1)
    bibtex_file = sys.argv[1]
    main(bibtex_file)
