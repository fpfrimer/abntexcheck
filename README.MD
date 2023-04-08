# abntexcheck

# Sumário

- [abntexcheck](#abntexcheck)
- [Sumário](#sumário)
  - [Introdução](#introdução)
  - [Pré-requisitos](#pré-requisitos)
  - [Instalação](#instalação)
  - [Uso](#uso)
  - [Desinstalação](#desinstalação)
  - [Suporte e contribuição](#suporte-e-contribuição)

## Introdução

O `abntexcheck` é uma ferramenta em Python para verificar a coerência das entradas BibTeX com as normas da ABNT (Associação Brasileira de Normas Técnicas). Ele analisa um arquivo BibTeX e informa campos obrigatórios e recomendados faltantes para cada entrada, ajudando os usuários a garantir que suas referências estejam de acordo com as diretrizes da ABNT.

Também verifica se existem substítulos implícitos em títulos e a existem de nomes de parentesco como Neto, Filho e Júnior que não podem ser considerados como sobrenomes.

## Pré-requisitos

Para utilizar o `abntexcheck`, certifique-se de que seu sistema atenda aos seguintes requisitos:

- Python 3.10 ou superior instalado.
- As seguintes bibliotecas Python instaladas:
  - pybtex: para leitura e análise de arquivos BibTeX;
  - re: para manipulação de expressões regulares;
  - argparse: para manipulação de argumentos.

Você pode instalar as bibliotecas necessárias usando o seguinte comando:

```bash
pip install <biblioteca>
```
**Nota**: O comando pip pode ser diferente em seu sistema (como pip3), dependendo da instalação do Python.

## Instalação

Siga os passos abaixo para instalar o `abntexcheck` no Linux:

1. Clone o repositório ou baixe o código-fonte do projeto:

```bash
git clone https://github.com/fpfrimer/abntexcheck.git
```

ou baixe diretamente como um arquivo ZIP e descompacte-o.

2. Navegue até a pasta do projeto:

```bash
cd abntexcheck
```

3. xecute o script de instalação:

```bash
./install.sh
```

O script copiará o arquivo abntbibcheck.py para um diretório no seu $PATH, permitindo que você execute o comando abntbibcheck em qualquer lugar no terminal. Além disso, analisará as dependências necessárias, se ainda não estiverem instaladas.

Após a instalação bem-sucedida, você deve ver uma mensagem de confirmação no terminal.

## Uso

Para usar o **abntexcheck**, execute o seguinte comando no terminal:

```bash
abntbibcheck [-h] [-c] <arquivo_bibtex>
```
onde:

  - '-h', '--help': (opcional) Exibe a mensagem de ajuda e sai.
  - '-c', '--color': (opcional) Ativa a saída colorida (desativado por padrão).
  - <arquivo_bibtex>: O caminho do arquivo BibTeX a ser analisado.

O **abntexcheck** informará campos obrigatórios e recomendados faltantes para cada entrada, além de verificar a existência de subtítulos implícitos nos títulos e possíveis designações de parentesco nos nomes dos autores.

**NOTA**: O nome do comando (abntbibcheck) é diferente do nome do repositório (abntexcheck).

## Desinstalação

Caso deseje desinstalar o abntexcheck, siga os passos abaixo:

1. Navegue até a pasta do projeto:

```bash
cd abntexcheck
```

2. Execute o script de desinstalação:

```bash
./uninstall.sh
```

O script removerá o arquivo abntbibcheck.py do diretório no seu $PATH. Após a desinstalação bem-sucedida, você deve ver uma mensagem de confirmação no terminal.

## Suporte e contribuição

Se você encontrar problemas ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma *issue* ou *pull request* no repositório do projeto no GitHub: https://github.com/fpfrimer/abntexcheck.

Agradecemos por usar e contribuir com o abntexcheck!