# Projeto Agenda Django 🚀

Este repositório contém o código fonte de um projeto de agenda desenvolvido com o framework Django. O objetivo deste projeto é fornecer uma aplicação robusta para gerenciar contatos e compromissos pessoais. 📅

## Funcionalidades 🌟

- 🔐 Cadastro de usuários e autenticação
- 📋 Gerenciamento de contatos com:
  - 🧑 Nome
  - 🗂️ Categoria
  - 📸 Foto
  - 📞 Dados adicionais como telefone e email
- ✏️ Criação, visualização, edição e exclusão de contatos
- 🏷️ Sistema de categorias para organização
- 📄 Paginação para listagem de contatos
- 💻 Interface responsiva e amigável

## Tecnologias Utilizadas 🛠️

- [Python](https://www.python.org/) 3.12.4 🐍
- [Django](https://www.djangoproject.com/) 5.1.4 🌐
- Banco de dados SQLite (configuração padrão, suportando PostgreSQL ou MySQL para produção)
- HTML, CSS e JavaScript para o front-end 🎨

## Pré-requisitos ✅

Antes de começar, certifique-se de ter o seguinte instalado na sua máquina:

- Python 3.12.4 🐍
- pip (gerenciador de pacotes do Python)
- Virtualenv (recomendado para isolamento do ambiente)

## Como Executar o Projeto ▶️

Siga os passos abaixo para executar o projeto localmente:

1. Clone o repositório:

```bash
git clone https://github.com/celiogomesdelima/projeto-agenda-django.git
```

2. Navegue até o diretório do projeto:

```bash
cd projeto-agenda-django
```

3. Crie um ambiente virtual e ative-o:

```bash
python -m venv venv
# No Windows
venv\Scripts\activate
# No Linux/MacOS
source venv/bin/activate
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Realize as migrações do banco de dados:

```bash
python manage.py migrate
```

6. Inicie o servidor local:

```bash
python manage.py runserver
```

7. Acesse a aplicação no navegador em: [http://localhost:8000](http://localhost:8000) 🌐

## Estrutura do Projeto 📂

```
projeto-agenda-django/
├── base_static/       # Arquivos estáticos globais
├── base_templates/    # Templates globais (layout base, mensagens, etc.)
├── contact/           # Aplicação principal de contatos
│   ├── templates/     # Templates específicos para contatos
│   ├── views/         # Lógica de visualização (views)
│   ├── forms.py       # Formulários
│   ├── models.py      # Modelos de dados
│   └── urls.py        # Rotas da aplicação
├── project/           # Configurações do projeto Django
├── manage.py          # Script de gerenciamento do Django
├── requirements.txt   # Dependências do projeto
└── README.md          # Documentação do projeto
```

## Contribuição 🤝

Contribuições são bem-vindas! Sinta-se à vontade para enviar issues ou pull requests para melhorias no projeto.

### Para contribuir:

1. Faça um fork do repositório
2. Crie uma branch para a sua feature:

```bash
git checkout -b minha-feature
```

3. Faça commit das suas alterações:

```bash
git commit -m 'Adiciona nova feature'
```

4. Envie suas alterações para o repositório remoto:

```bash
git push origin minha-feature
```

5. Abra um Pull Request no GitHub

## Licença 📄

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

Desenvolvido por [Célio Gomes de Lima](https://github.com/celiogomesdelima). ❤️
