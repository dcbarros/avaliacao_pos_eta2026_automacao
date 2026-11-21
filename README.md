# Avaliação final da matéria de Automação de Testes

Trabalho de pós-graduação da disciplina de Automação de Testes.

**Professor** — FERNANDO BENBASSAT

**Integrantes**

- Davison Cavalcante
- José Maciel
- Marcus Vinicius
- Michelle Silva

## XYZ Bank

O projeto usa o XYZ Bank, uma aplicação bancária de demonstração da GlobalSQA. A aplicação tem duas áreas: a do gerente, onde é possível cadastrar clientes e abrir contas, e a do cliente, onde é possível selecionar uma conta, fazer depósitos e saques e consultar o extrato.

A suíte usa Python, pytest e Selenium para automatizar esses fluxos pelo navegador. Os cenários ficam em `tests/`, os Page Objects em `pages/` e o gerenciamento da sessão do navegador em `core/`.

[Acessar o XYZ Bank](https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login)

## Como usar o repositório

### Pré-requisitos

- Git e Python 3.12 com pip.
- Google Chrome instalado.
- Acesso à internet para instalar as dependências, acessar o XYZ Bank e permitir que o Selenium obtenha o ChromeDriver quando necessário.

### Instalação

Clone o repositório, entre na pasta do projeto e crie um ambiente virtual.

```bash
git clone https://github.com/dcbarros/avaliacao_pos_eta2026_automacao.git
cd avaliacao_pos_eta2026_automacao
python -m venv .venv
```

Ative o ambiente virtual. No Linux ou macOS, use:

```bash
source .venv/bin/activate
```

No Windows PowerShell, use:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências com o ambiente virtual ativo.

```bash
python -m pip install -r requirements.txt
```

### Execução dos testes

Na raiz do repositório, execute toda a suíte com:

```bash
python -m pytest -v
```

Para executar um único cenário, indique o arquivo. Por exemplo, o CT15 verifica o aviso exibido para um cliente sem conta.

```bash
python -m pytest -v tests/test_ct15.py
```

Para rodar a suíte sem abrir uma janela do Chrome, defina `HEADLESS=1`. No Linux ou macOS, use:

```bash
HEADLESS=1 python -m pytest -v
```

No Windows PowerShell, use:

```powershell
$env:HEADLESS = "1"
python -m pytest -v
```
