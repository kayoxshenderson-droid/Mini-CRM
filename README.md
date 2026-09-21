# Mini-CRM de Leads

Um sistema simples de gerenciamento de leads via linha de comando feito em Python. O objetivo do projeto é servir como uma ferramenta direta e leve para cadastrar contatos comerciais, acompanhar a etapa de cada um no funil de vendas e exportar relatórios em CSV sem precisar de dependências externas ou configurações complexas.

---

## O que o sistema faz

- Cadastro de novos leads com nome, e-mail e etapa do funil.
- Gravação automática da data de cadastro.
- Validação para evitar campos vazios, e-mails inválidos ou registros duplicados.
- Visualização de toda a base em formato de tabela no terminal.
- Busca rápida por nome ou endereço de e-mail.
- Exportação da base de leads para arquivo CSV compatível com Excel e Google Sheets.
- Armazenamento local em JSON, sem necessidade de banco de dados externo.

---

## Estrutura do projeto

O código foi organizado seguindo a separação básica de responsabilidades (padrão MVC):

```text
Mini-CRM/
│
├── data/
│   ├── leads.json         # Base de dados em JSON
│   └── leads.csv          # Arquivo gerado ao exportar
│
├── model.py               # Estrutura e padronização dos dados do lead
├── control.py             # Lógica de persistência, leitura, busca e exportação
├── app.py                 # Menu interativo e interface no terminal
│
├── control_completo.py    # Versão do controller com validações extras
├── app_completo.py        # Versão do app com mensagens e tratamento de erros
└── README.md              # Documentação do projeto
```

---

## Como rodar o projeto

### Requisitos
- Python 3.10 ou superior instalado.
- Apenas bibliotecas nativas do Python (`pathlib`, `json`, `csv`, `datetime`), sem necessidade de `pip install`.

### Executando

1. Clone o repositório ou baixe os arquivos:
   ```bash
   git clone https://github.com/seu-usuario/Mini-CRM.git
   cd Mini-CRM
   ```

2. Execute o script principal:
   ```bash
   python app.py
   ```
   *(ou para rodar a versão com validações completas: `python app_completo.py`)*

---

## Exemplo de uso

Ao rodar a aplicação, o seguinte menu é exibido:

```text
=== Mini CRM de Leads ===
[1] Adicionar lead
[2] Listar leads
[3] Buscar (nome/e-mail)
[4] Exportar para CSV
[0] Sair do programa

Escolha uma opção: 2

============================================================
## | Nome            | E-mail                 | Etapa
------------------------------------------------------------
00 | Carlos Silva    | carlos@empresa.com     | Proposta
01 | Mariana Souza   | mariana@startup.io     | Fechado
02 | Roberto Lima    | roberto@tech.com       | Contato
============================================================
```

---

## Ideias de melhorias futuras

- Adicionar persistência com SQLite.
- Implementar edição e exclusão de contatos direto pelo menu.
- Adicionar filtros por etapa do funil.
- Criar uma interface web básica com Flask ou Streamlit.

---

## Licença

Projeto sob licença MIT. Sinta-se livre para usar e modificar.
