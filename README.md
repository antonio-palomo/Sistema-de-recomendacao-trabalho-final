# Sistema-de-recomendacao-trabalho-final
Trabalho final da matéria Desenvolvimento de Sistemas de IA

Claro! Aqui está um `README.md` completo, explicando cada parte do sistema, cobrindo a estrutura do código, execução com Docker, e alinhado com os requisitos da atividade acadêmica que você descreveu:

---

```markdown
# 🎬 Sistema de Recomendação com FastAPI e Docker

## 📌 Objetivo

Este projeto tem como objetivo o desenvolvimento de um sistema de recomendação de filmes utilizando o dataset **MovieLens**, com uma API construída em **FastAPI** e containerizada com **Docker**.

A proposta segue as etapas práticas de um sistema real, oferecendo recomendações com base nas preferências de usuários.

---

## 📁 Estrutura do Projeto

```

📦 sistema-recomendacao/
├── main.py               # Inicialização da API FastAPI e definição dos endpoints
├── recommender.py        # Lógica do sistema de recomendação (content-based)
├── schemas.py            # Modelos Pydantic para validação de entrada/saída da API
└── data/
│ings.csv       # Dataset MovieLens com avaliações de filmes por usuários
│   └── movies.csv        # Dataset MovieLens com informações dos filmes
├── Dockerfile                # Instruções para construir o container da aplicação
├── requirements.txt          # Dependências do projeto Python
└── README.md                 # Documentação do projeto

````

---

## 🧠 Modelo de Recomendação

O sistema utiliza **filtragem baseada em conteúdo**:

- Os gêneros dos filmes são usados como **features**.
- As preferências dos usuários são extraídas com base nos filmes avaliados.
- A similaridade é calculada usando **cosseno** entre o perfil médio dos filmes curtidos e os demais filmes do sistema.
- Recomendamos os filmes mais similares que o usuário ainda **não assistiu**.

---

## 🚀 Endpoints da API

Documentação interativa disponível via Swagger em: `http://localhost:8000/docs`

### 📩 `POST /recommend`
Recomenda filmes para um usuário com base em suas preferências.

```json
{
  "user_id": 1,
  "n": 5
}
````

### ➕ `POST /user/{user_id}`

Adiciona um novo usuário (não obrigatório com o dataset MovieLens, pois já estão carregados).

### ➕ `POST /item`

Adiciona um novo item manualmente, com features personalizadas.

### 🛠️ `PUT /user/preferences`

Atualiza os itens curtidos por um usuário.

```json
{
  "user_id": 1,
  "liked_items": [1, 50, 100]
}
```

---

## 🐳 Executando com Docker

### Pré-requisitos

* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)

### 1. Clonar o projeto

```bash
git clone https://github.com/seu-usuario/sistema-recomendacao.git
cd sistema-recomendacao
```

### 2. Adicionar os datasets

Baixe os arquivos `movies.csv` e `ratings.csv` do site oficial [GroupLens](https://grouplens.org/datasets/movielens/) e coloque dentro de `app/data/`.

### 3. Build da imagem Docker

```bash
docker build -t sistema-recomendacao .
```

### 4. Rodar a aplicação

```bash
docker run -p 8000:8000 sistema-recomendacao
```

Agora acesse `http://localhost:8000/docs` para testar os endpoints.

---

## 🧪 Testes

Você pode escrever testes utilizando `pytest`, simulando chamadas aos endpoints com a lib `TestClient` do FastAPI.

**Exemplo de teste básico (`test_api.py`)**:

```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_recommendation():
    response = client.post("/recommend", json={"user_id": 1, "n": 5})
    assert response.status_code == 200
    assert "recommendations" in response.json()
```

---

## 📄 Tecnologias Utilizadas

* **Python 3.10+**
* **FastAPI**
* **pandas**
* **scikit-learn**
* **Docker**

---

## 📚 Desenho do Sistema

| Componente       | Descrição                                                                    |
| ---------------- | ---------------------------------------------------------------------------- |
| `recommender.py` | Contém a lógica do modelo de recomendação baseado em conteúdo.               |
| `schemas.py`     | Define os modelos de entrada e saída da API com `Pydantic`.                  |
| `main.py`        | Contém os endpoints da API e inicializa o sistema com os dados do MovieLens. |

---

## 📦 Requisitos

### Arquivo `requirements.txt`

```txt
fastapi
uvicorn
pandas
scikit-learn
```

---

## 📄 Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY ./app /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## ✅ Entregáveis

* ✅ API funcional com recomendações baseadas em conteúdo
* ✅ Swagger para testes interativos
* ✅ Dockerfile para containerização
* ✅ Dataset público (MovieLens) integrado
* ✅ README explicando execução, arquitetura e uso
* ✅ Pontos de extensão: adição manual de usuários e itens, testes automatizados

---

## 🎓 Créditos

Projeto desenvolvido para fins educacionais na disciplina de **Sistemas Inteligentes / Recomendação**, com foco em práticas modernas de desenvolvimento, deployment e recomendação inteligente.

---

```

Se quiser, posso empacotar esse projeto todo (estrutura + código + Dockerfile + README) num `.zip` pronto para rodar localmente. Deseja isso?
```
