# 🍰 Projeto Confeitaria

Sistema de gerenciamento para uma confeitaria, desenvolvido em **Django** e **Django REST Framework**.  
Permite cadastrar **clientes, produtos, endereços e pedidos**, com interface web e API REST.

---

## 🚀 Funcionalidades

- **Clientes**
  - Cadastro de clientes com nome, telefone e email
  - Endereços associados a cada cliente
  - Visualização de detalhes

- **Produtos**
  - Cadastro de produtos com descrição, preço e disponibilidade
  - Controle de estoque
  - Visualização de detalhes

- **Pedidos**
  - Registro de pedidos vinculados a clientes
  - Itens do pedido com quantidade e subtotal
  - Cálculo automático do valor total
  - Detalhes do pedido com forma de pagamento e datas

- **API REST**
  - Endpoints para clientes, produtos, endereços e pedidos
  - Suporte a operações CRUD (Create, Read, Update, Delete)

---

## 🛠️ Tecnologias utilizadas

- [Python](https://www.python.org/) 3.14
- [Django](https://www.djangoproject.com/) 6.0.1
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Bootstrap 5](https://getbootstrap.com/) para estilização

---

## 📦 Instalação e execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/projeto-confeitaria.git
   cd projeto-confeitaria
   ```

2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute as migrações:
   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

6. Acesse no navegador:
   - Interface web: `http://127.0.0.1:8000/` [(127.0.0.1 in Bing)](https://www.bing.com/search?q="http%3A%2F%2F127.0.0.1%3A8000%2F")
   - API REST: `http://127.0.0.1:8000/api/` [(127.0.0.1 in Bing)](https://www.bing.com/search?q="http%3A%2F%2F127.0.0.1%3A8000%2Fapi%2F")

---

## 📂 Estrutura do projeto

```
Projeto-Confeitaria/
├── clientes/        # App de clientes
├── produtos/        # App de produtos
├── pedidos/         # App de pedidos
├── enderecos/       # App de endereços
├── templates/       # Templates HTML (Bootstrap)
├── core/            # Configurações principais
└── README.md
```

---

## 🔗 Rotas principais

### Web
- `/clientes/` → lista de clientes
- `/clientes/<id>/` → detalhe do cliente
- `/produtos/` → lista de produtos
- `/produtos/<id>/` → detalhe do produto
- `/pedidos/` → lista de pedidos
- `/pedidos/<id>/` → detalhe do pedido

### API REST
- `/api/clientes/`
- `/api/produtos/`
- `/api/pedidos/`
- `/api/enderecos/`

---

## 👨‍💻 Autores

Projeto desenvolvido por **Gustavo / Flavia / Evelyne / Gabriel** como prática de Django + DRF.  
```

---
