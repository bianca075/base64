# Base64 Encoder/Decoder em Python

Este repositório contém uma implementação simples de um codificador/decodificador Base64 em Python, feita **sem usar bibliotecas externas**. O foco é didático: mostrar, passo a passo, como funciona a conversão de texto para Base64 e o caminho inverso.

## Funcionalidades

- Codificação de texto para Base64 (`codificar(texto)`)
- Decodificação de Base64 para texto (`decodificar(base64_texto)`)
- Interface simples via linha de comando para testar o algoritmo

## Estrutura do Projeto

- `base64.py`  
  Contém:
  - A tabela Base64 padrão (`TABELA_BASE64`)
  - A função `codificar(texto)`, que:
    - Converte cada caractere em ASCII
    - Transforma para binário (8 bits)
    - Agrupa os bits em blocos de 6
    - Usa a tabela Base64 para gerar a string codificada
    - Ajusta o padding com `=` para múltiplos de 4
  - A função `decodificar(base64_texto)`, que:
    - Remove o padding `=`
    - Converte cada caractere Base64 em índice (0–63)
    - Transforma para binário (6 bits)
    - Reagrupa em bytes (8 bits)
    - Converte de volta para caracteres de texto
  - Um teste simples no bloco `if __name__ == "__main__":`

## Pré-requisitos

- Python 3.x instalado na máquina

Você pode verificar a versão do Python com:

```bash
python --version
# ou
python3 --version
```

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repo-base64.git
cd seu-repo-base64
```

2. Execute o script:

```bash
python base64.py
# ou
python3 base64.py
```

3. Quando o programa pedir a entrada, digite um texto para ser codificado em Base64.

Exemplo:

```text
Digite uma palavra para codificar: Ola
Codificada: T2xh
Decodificada: Ola
```

## Como Usar no Seu Código

Você também pode importar as funções em outros scripts Python:

```python
from base64 import codificar, decodificar

texto = "Hello"
codificada = codificar(texto)
print(codificada)           # saída: SGVsbG8=
print(decodificar(codificada))  # saída: Hello
```

## Objetivo do Projeto

Este projeto foi criado com propósito educativo, para:

- Entender a lógica por trás da Base64 sem depender de bibliotecas prontas
- Servir como exemplo simples para estudos de manipulação de bits em Python
- Compor um portfólio de código limpo, comentado e fácil de entender
