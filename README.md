# 🚀 Lead Management API

RESTful API desenvolvida em Python utilizando Flask para gerenciamento de leads.

---

## 📌 Sobre o projeto

Este projeto simula um sistema real de captação e gerenciamento de leads, com operações completas de CRUD, validação de dados e arquitetura em camadas.

---

## 🧠 Arquitetura

O projeto segue uma arquitetura organizada em camadas:

* **Routes** → define os endpoints da API
* **Services** → contém regras de negócio
* **Repositories** → acesso ao banco de dados
* **Utils** → validações e logs

---

## 🛠️ Tecnologias utilizadas

* Python
* Flask
* SQLite
* REST API

---

## ⚙️ Funcionalidades

* Criar leads
* Listar leads
* Buscar lead por ID
* Atualizar lead
* Deletar lead
* Validação de dados
* Logging de operações

---

## ▶️ Como rodar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/daivin11/lead-management-api.git
cd lead-management-api
```

---

### 2. Criar ambiente virtual

```bash
python -m venv .venv
source .venv/Scripts/activate
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Rodar o servidor

```bash
python app.py
```

---

## 🌐 Endpoints

### 🔹 Criar lead

POST `/leads`

```json
{
  "nome": "Maria",
  "email": "maria@email.com",
  "interesse": "Consultoria",
  "valor": 3000
}
```

---

### 🔹 Listar leads

GET `/leads`

---

### 🔹 Buscar lead por ID

GET `/leads/{id}`

---

### 🔹 Atualizar lead

PUT `/leads/{id}`

---

### 🔹 Deletar lead

DELETE `/leads/{id}`

---

## 📊 Exemplo de resposta

```json
{
  "status": "success",
  "message": "Lead criado",
  "data": {
    "id": 1
  }
}
```

---

## 📁 Estrutura do projeto

```
lead-management-api/
├── app.py
├── database.py
├── routes/
│   └── lead_routes.py
├── services/
│   └── lead_service.py
├── repositories/
│   └── lead_repository.py
├── utils/
│   ├── logger.py
│   └── validators.py
├── requirements.txt
```

---

## 💼 Objetivo

Projeto desenvolvido com foco em simular práticas reais de desenvolvimento backend utilizadas em empresas, incluindo arquitetura em camadas, validação, logging e organização de código.

---

## 👨‍💻 Autor

David Soares
