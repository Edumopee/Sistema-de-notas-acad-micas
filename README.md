# Sistema de Gerenciamento de Notas Acadêmicas

Este é um sistema de linha de comando (CLI) desenvolvido em Python para automatizar o gerenciamento de notas escolares. O objetivo principal do projeto é permitir o cadastro seguro de estudantes através de um identificador único (RA), além de calcular médias aritméticas e validar a situação de aprovação institucional com base nos critérios estabelecidos.

O projeto foi construído seguindo boas práticas de desenvolvimento, como o Princípio de Responsabilidade Única (SRP), padronização de nomenclatura PEP 8 (`snake_case`) e documentação interna via Docstrings.

---

## 🚀 Funcionalidades
* **Cadastro de Estudantes:** Permite registrar o RA, o Nome e múltiplas notas de forma dinâmica.
* **Validação de Duplicidade:** O sistema impede o cadastro de dois alunos com o mesmo RA.
* **Tratamento de Erros:** Proteção contra digitação de notas inválidas (fora do intervalo de 0 a 10) ou caracteres não numéricos.
* **Cálculo Automatizado de Média:** Motor lógico que calcula a média aritmética de forma robusta.
* **Relatório Final:** Exibição detalhada com RA, Nome, Notas, Média Final e Status Institucional (Aprovado/Reprovado).

---

## 📋 Pré-requisitos
Para executar este projeto, você precisará apenas do ambiente de execução do Python instalado em sua máquina.
* **Python 3.8** ou superior.
Nenhuma biblioteca externa adicional é necessária, pois o sistema utiliza apenas módulos nativos do Python.

---

## 🔧 Como Executar o Código Principal
Siga os passos abaixo para rodar a aplicação a partir do seu terminal:
1. Abra o terminal na pasta onde o arquivo `main.py` está salvo.
2. Execute o comando abaixo para iniciar o menu interativo:
   python main.py
3. No menu exibido, escolha a opção desejada digitando o número correspondente (`1` para Cadastrar, `2` para Exibir Relatório ou `3` para Sair) e pressione Enter.

---

## 🧪 Como Acionar o Ambiente de Testes
Para validar o comportamento do motor lógico manualmente:
1. Digite `python` no seu terminal para abrir o interpretador interativo.
2. Importe e teste as funções com o exemplo abaixo:

```python
from main import calcular_media, verificar_aprovacao
