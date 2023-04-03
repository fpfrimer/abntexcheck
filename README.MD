# abntexcheck

O `abntexcheck` é uma ferramenta em Python para verificar a coerência das entradas BibTeX com as normas da ABNT (Associação Brasileira de Normas Técnicas). Ele analisa um arquivo BibTeX e informa campos obrigatórios e recomendados faltantes para cada entrada, ajudando os usuários a garantir que suas referências estejam de acordo com as diretrizes da ABNT.

## Pré-requisitos

Para utilizar o `abntexcheck`, certifique-se de que seu sistema atenda aos seguintes requisitos:

- Python 3.10 ou superior instalado.
- As seguintes bibliotecas Python instaladas:
  - pybtex: para leitura e análise de arquivos BibTeX.
  - re: para manipulação de expressões regulares.

Você pode instalar as bibliotecas necessárias usando o seguinte comando:

```bash
pip install pybtex
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

O script copiará o arquivo abntbibcheck.py para um diretório no seu $PATH, permitindo que você execute o comando abntbibcheck em qualquer lugar no terminal. Além disso, ele instalará as dependências necessárias, se ainda não estiverem instaladas.

Após a instalação bem-sucedida, você deve ver uma mensagem de confirmação no terminal.