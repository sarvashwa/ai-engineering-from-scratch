# AI Engineering From Scratch

A production-style AI engineering project built from first principles.

Rather than relying on orchestration frameworks such as LangChain or LlamaIndex, this repository incrementally implements the core building blocks behind modern AI systems—including API design, embeddings, vector databases, semantic retrieval, prompt engineering, local LLM orchestration, and Retrieval-Augmented Generation (RAG).

The objective is not only to build AI applications, but to understand **why** each component exists, **how** it works internally, and **how** production-grade AI systems are architected.

---

# Philosophy

This project follows a small set of engineering principles throughout its development.

* Build from first principles before introducing abstractions.
* Learn architecture before learning frameworks.
* Keep each class responsible for one concern.
* Prefer composition over inheritance.
* Separate business logic from infrastructure.
* Introduce abstractions only when repetition appears.
* Build production-quality software, not tutorials.

---

# Current Features

## Core Architecture

* Modular service-oriented architecture
* Composition Root (Application Bootstrap)
* API Composition using APIRouter
* Dependency Injection
* Clean separation of responsibilities
- Centralized route registration

## API Layer

- FastAPI REST API
- Modular routing with APIRouter
- Thin endpoint architecture
- Request validation using Pydantic
- Response validation using Pydantic
- Automatic OpenAPI schema generation
- Interactive Swagger documentation
- Health check endpoint

## AI Components

Current implementation is being developed incrementally.

Planned components include:

* Local LLM inference using Ollama
* LiteLLM integration
* Sentence Transformer embeddings
* ChromaDB vector database
* Semantic retrieval
* Prompt engineering
* Retrieval-Augmented Generation (RAG)

---

# Design Rules

The project follows a few architectural rules to keep the codebase maintainable.

- The application is assembled only once in the Composition Root.
- Business services never depend on FastAPI.
- API routes remain thin and delegate business logic to services.
- Request and response schemas belong to the API layer.
- Domain models remain independent of HTTP concerns.
- Shared configuration is centralized rather than duplicated.

---

# Current Architecture

```                    
                    Client
                       │
                  HTTP Request
                       │
                       ▼
                  FastAPI (main.py)
                       │
                include_router()
                       │
                       ▼
                  API Router
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
     Health Router             Ask Router
          │                         │
          ▼                         ▼
     GET /health              POST /ask
                                    │
                                    ▼
                               AskRequest
                                    │
                                    ▼
                               RAGService
                                    │
                                    ▼
                               AskResponse
                                    │
                                    ▼
                               JSON Response
```

The current implementation focuses on building a clean API layer before introducing retrieval pipelines, vector databases, and LLM integrations.

---

# Planned Architecture

```text
                    Client
                       │
                       ▼
                  FastAPI
                       │
                  API Router
                       │
                       ▼
                  RAG Service
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
 RetrievalService  PromptBuilder  LLMService
        │                             │
        ▼                             ▼
 EmbeddingService                LiteLLM
        │                             │
        ▼                             ▼
    ChromaDB                     Ollama
```

This architecture will evolve naturally as new components are implemented.

---

# Project Structure

```text
src/
├── api/
│   ├── router.py
│   ├── dependencies.py
│   ├── exceptions.py
│   ├── middleware.py
│   ├── routes/
│   │   ├── ask.py
│   │   └── health.py
│   │
│   └── schemas/
│       ├── ask_request.py
│       ├── ask_response.py
│       └── health_response.py
│
├── application/
│   ├── application.py
│   └── bootstrap.py
│
├── config/
│
├── models/
│
├── services/
│
├── storage/
│
├── main.py
│
experiments/
│
README.md
requirements.txt
```

| Directory      | Responsibility                                                               |
| -----------    | -----------------------------------------------------------------------------|
| application    | Composition Root and Dependency Injection                                    |
| api/routes     | HTTP endpoints grouped by feature                                            |
| api/schemas    | Request and response models                                                  |
| api/router.py  | Central API router that composes all route modules                           |
| services       | Business logic                                                               |
| storage        | Persistence and Vector storage and persistence                               |
| models         | Domain models (business entities)                                            |
| config         | Application configuration                                                    |
| experiments    | Learning and validation experiments                                          |

---

# Technology Stack

| Category          | Technology                        |
| ----------------- | --------------------------------- |
| Language          | Python 3.13                       |
| API               | FastAPI                           |
| Validation        | Pydantic                          |
| ASGI Server       | Uvicorn                           |
| Local LLM         | Ollama *(planned)*                |
| LLM Abstraction   | LiteLLM *(planned)*               |
| Vector Database   | ChromaDB *(planned)*              |
| Embeddings        | Sentence Transformers *(planned)* |
| Embedding Backend | FastEmbed *(planned)*             |

---

# Installation

Clone the repository.

```bash
git clone <repository-url>
cd <repository-name>
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Install dependencies.

```bash
python -m pip install -r requirements.txt
```

---

# Running the API

Start the development server.

```bash
uvicorn src.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

# Running Experiments

Individual concepts are also implemented as standalone experiments.

Example:

```bash
python -m experiments.12_bootstrap
```

Experiments provide isolated implementations before concepts are integrated into the main application.

---
# Dependency Injection

The application uses FastAPI's dependency injection system to provide application services to API endpoints.

Dependencies are resolved through dedicated provider functions located in `src/api/dependencies.py`.

This keeps endpoints focused on handling HTTP requests while business logic remains inside service classes.

The project follows the principle of injecting the smallest dependency required rather than exposing the entire application object whenever possible.

---

# Engineering Principles

This project intentionally avoids hiding complexity behind high-level frameworks during the initial stages.

Each major component is implemented independently to understand the engineering decisions behind modern AI systems, including:

* Dependency Injection
* Composition Root
* Service-Oriented Architecture
* API Design
* Embedding Pipelines
* Vector Databases
* Semantic Search
* Prompt Engineering
* Retrieval-Augmented Generation

---

# Roadmap

## Foundation

* ✅ Project structure
* ✅ Composition Root
* ✅ FastAPI
* ✅ APIRouter
* ✅ Request models
* ✅ Response models
* ✅ Health endpoint
* ✅ Thin endpoint architecture

## API

## API

* ✅ OpenAPI & Swagger
* ✅ Health endpoint
* ✅ Dependency Injection with Depends
* ⬜ Exception handling
* ⬜ Configuration management
* ⬜ Logging
* ⬜ API versioning

## AI Pipeline

* ⬜ Ollama integration
* ⬜ LiteLLM
* ⬜ Embedding service
* ⬜ ChromaDB
* ⬜ Document ingestion
* ⬜ Semantic retrieval
* ⬜ Prompt builder
* ⬜ RAG pipeline

## Advanced Features

* ⬜ Streaming responses
* ⬜ Conversation memory
* ⬜ Evaluation framework
* ⬜ Hybrid search
* ⬜ Authentication
* ⬜ Docker
* ⬜ CI/CD
* ⬜ Production deployment

---

# License

This project is released under the MIT License.
