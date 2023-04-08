# abntexcheck

Versão v1.0.0-alpha
**Nota**: Código criado com auxílio parcial de inteligencia artificial.

# Sumário

- [abntexcheck](#abntexcheck)
- [Sumário](#sumário)
  - [Introdução](#introdução)
  - [Pré-requisitos](#pré-requisitos)
  - [Instalação em ambiente Linux](#instalação-em-ambiente-linux)
    - [Uso](#uso)
    - [Desinstalação](#desinstalação)
  - [Instalação no Windows](#instalação-no-windows)
    - [Criando um arquivo .bat e adicionando o diretório ao PATH no Windows](#criando-um-arquivo-bat-e-adicionando-o-diretório-ao-path-no-windows)
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

## Instalação em ambiente Linux

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

### Uso

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

### Desinstalação

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

## Instalação no Windows

Siga os passos abaixo para instalar o abntexcheck no Windows:

1. Certifique-se de que você tenha o Python 3.10 ou superior instalado. Caso ainda não tenha instalado, você pode baixá-lo no site oficial do Python. Durante a instalação, marque a opção "Add Python to PATH" para facilitar o uso do Python no prompt de comando.
2. Instale as bibliotecas necessárias. Abra o Prompt de Comando (cmd) ou o PowerShell e execute o seguinte comando:

```bash
pip install pybtex argparse re
```

**Nota**: O comando pip pode ser diferente no seu sistema (como pip3), dependendo da instalação do Python.

3. Clone o repositório ou baixe o código-fonte do projeto:

```bash
git clone https://github.com/fpfrimer/abntexcheck.git
```
ou baixe diretamente como um arquivo ZIP e descompacte-o.

4. Copie o arquivo abntbibcheck.py para um diretório no seu PATH ou crie um atalho para ele. Você pode copiar o arquivo para a pasta Scripts do Python (geralmente localizada em C:\Python<versão>\Scripts) ou para qualquer outro diretório que esteja no PATH do sistema.
5. Agora você pode executar o abntexcheck usando o Prompt de Comando (cmd) ou o PowerShell navegando até o diretório onde o arquivo abntbibcheck.py foi copiado e executando:

```bash
python abntbibcheck.py <arquivo_bibtex>
```

Substitua <arquivo_bibtex> pelo caminho do arquivo BibTeX que você deseja verificar.

### Criando um arquivo .bat e adicionando o diretório ao PATH no Windows

Caso queira, você pode criar um arquivo .bat para executar o código python. Adicionalmente, você pode adicionar esses arquivos ao PATH do Windows para executar de qualquer diretório. Para isso, siga as seguintes instruções:

1. Navegue até o diretório onde você salvou o arquivo abntbibcheck.py. Crie um novo arquivo de texto chamado abntbibcheck.bat no mesmo diretório.
2. bra o arquivo abntbibcheck.bat com um editor de texto e adicione o seguinte conteúdo:

```bat
@echo off
python "%~dp0\abntbibcheck.py" %*
```
3. Salve e feche o arquivo.

4. Agora, adicione o diretório que contém o arquivo abntbibcheck.bat e abntbibcheck.py.bat ao PATH do sistema. Siga estas etapas:


   1. Abra o Painel de Controle e vá para "Sistema e Segurança" > "Sistema" > "Configurações avançadas do sistema".

   2. Na guia "Avançado", clique no botão "Variáveis de Ambiente".

   3. Na seção "Variáveis do sistema", procure pela variável "Path" e selecione-a. Clique no botão "Editar".

   4. Clique no botão "Novo" e adicione o caminho completo do diretório que contém o arquivo abntbibcheck.bat. Por exemplo, C:\caminho\para\o\diretorio.

   5. Clique em "OK" para fechar todas as janelas abertas.

5. Feche e reabra o Prompt de Comando (cmd) ou o PowerShell para que as alterações entrem em vigor.
6. Agora você pode executar o abntbibcheck em qualquer lugar usando o Prompt de Comando (cmd) ou o PowerShell com o seguinte comando:

```
abntbibcheck <arquivo_bibtex>
```
Substitua <arquivo_bibtex> pelo caminho do arquivo BibTeX que você deseja verificar.

## Suporte e contribuição

Se você encontrar problemas ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma *issue* ou *pull request* no repositório do projeto no GitHub: https://github.com/fpfrimer/abntexcheck.

Agradecemos por usar e contribuir com o abntexcheck!