# Sistema-de-recomendacao-trabalho-final
Trabalho final da matéria Desenvolvimento de Sistemas de IA

# Sistema de Recomendação com FastAPI e Docker

## Objetivo

Este projeto tem como objetivo o desenvolvimento de um sistema de recomendação de filmes utilizando o dataset **MovieLens**, com uma API construída em **FastAPI** e containerizada com **Docker**.

A proposta segue as etapas práticas de um sistema real, oferecendo recomendações com base nas preferências de usuários.

## Estrutura do Projeto:
sistema-de-recomendacao-trabalho-final/
├── main.py               # Inicialização da API FastAPI e definição dos endpoints
├── recommender.py        # Lógica do sistema de recomendação (content-based)
├── schemas.py            # Modelos Pydantic para validação de entrada/saída da API
├── Dockerfile                # Instruções para construir o container da aplicação
├── requirements.txt          # Dependências do projeto Python
└── README.md                 # Documentação do projeto

## Modelo de Recomendação

O sistema utiliza **filtragem baseada em conteúdo**:

- Os gêneros dos filmes são usados como **features**.
- As preferências dos usuários são extraídas com base nos filmes avaliados.
- A similaridade é calculada usando **cosseno** entre o perfil médio dos filmes curtidos e os demais filmes do sistema.
- Recomendamos os filmes mais similares que o usuário ainda **não assistiu**.

## Endpoints da API

Documentação interativa disponível via Swagger em: `http://localhost:8000/docs`

### `POST /recommend`
Recomenda filmes para um usuário com base em suas preferências.

```json
{
  "user_id": 1,
  "n": 5
}
````

## `POST /user/{user_id}`

Adiciona um novo usuário.

## `POST /item`

Adiciona um novo item manualmente, com features personalizadas.

### `PUT /user/preferences`

Atualiza os itens curtidos por um usuário.

```json
{
  "user_id": 1,
  "liked_items": [1, 50, 100]
}
```

---

## Executando com Docker

### Pré-requisitos

* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)

### 1. Clonar o projeto

```bash
git clone https://github.com/antonio-palomo/Sistema-de-recomendacao-trabalho-final
cd sistema-recomendacao
```

### 2. Build da imagem Docker

```bash
docker build -t sistema-recomendacao .
```

### 3. Rodar a aplicação

```bash
docker run -p 8000:8000 sistema-recomendacao
```

Agora acesse `http://localhost:8000/docs` para testar os endpoints.

## Tecnologias Utilizadas

* **Python 3.10+**
* **FastAPI**
* **pandas**
* **scikit-learn**
* **Docker**

## Desenho do Sistema

| Componente       | Descrição                                                                    |
| ---------------- | ---------------------------------------------------------------------------- |
| `recommender.py` | Contém a lógica do modelo de recomendação baseado em conteúdo.               |
| `schemas.py`     | Define os modelos de entrada e saída da API com `Pydantic`.                  |
| `main.py`        | Contém os endpoints da API e inicializa o sistema com os dados do MovieLens. |

## Requisitos

### Arquivo `requirements.txt`

```txt
fastapi
uvicorn
pandas
scikit-learn
```
## Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY ./app /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Para execução do código utilizei o ambiente do github se fizer desta forma basta clonar o respositorio e criar no main branch um codespace basta então rodar o docker e iniciar o ambiente com os códigos acima.
