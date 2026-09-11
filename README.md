# SME Finance Operations AI

[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688.svg?style=flat&logo=fastapi)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-18-61DAFB.svg?style=flat&logo=react)](https://react.dev)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB.svg?style=flat&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> **Automated Credit Underwriting & Cash Flow Forecasting for Emerging Markets**

An AI-powered operational finance platform for small & medium enterprises (SMEs). Features automated credit scoring, Debt Service Coverage Ratio (DSCR) underwriting, cash flow anomaly detection, and credit facility recommendations.

---

## 🏛️ Clean Architecture Overview

This repository is built following **Clean Layered Architecture** standards:

```
apps/api/app/
├── api/          # Thin REST routers & Dependency Injection (deps.py)
├── schemas/      # Pydantic v2 validation DTOs (Request / Response)
├── models/       # SQLAlchemy 2.0 Async ORM models & Base declarative metadata
├── repositories/ # Dedicated async database access queries ONLY
├── services/     # Pure business logic, domain rules, & AI orchestrators
├── core/         # Settings (pydantic-settings), Async Database, JWT Security, & Exceptions
└── utils/        # Reusable helper utilities
```

---

## ✨ Key Features

- **Automated Underwriting**:  DSCR cash-flow verification & credit risk classification
- **Ledger Analytics**:  Async tracking of enterprise revenue, expenses, and net margins
- **Financial Dashboard**:  Dynamic React 18 frontend with cash flow telemetry and credit gauges
- **Enterprise Security**:  OAuth2 JWT authentication & role-based security access

---

## 🛠️ Tech Stack

- **Backend**: Python 3.12, FastAPI 0.110+, Async SQLAlchemy 2.0+, Pydantic v2
- **Frontend**: React 18, TypeScript, Tailwind CSS, Lucide Icons
- **Database & Cache**: PostgreSQL (Asyncpg), Redis, Elasticsearch
- **AI & RAG**: vLLM / Ollama, LangChain, LangGraph State Graphs
- **DevOps & Testing**: Docker, Docker Compose, Pytest, Pytest-Asyncio

---

## 🚀 Quick Start Guide

### 1. Prerequisites
- Docker & Docker Compose
- Python 3.12+
- Node.js 20+

### 2. Backend Setup
```bash
# Navigate to API directory
cd apps/api

# Install dependencies
pip install -r requirements.txt

# Run database migrations & start FastAPI app
python main.py
# API running at http://localhost:8000 (Swagger docs at http://localhost:8000/docs)
```

### 3. Frontend Setup
```bash
# Navigate to Web app directory
cd apps/web

# Install dependencies & start dev server
npm install
npm run dev
# Web app running at http://localhost:3000
```

### 4. Running via Docker Compose
```bash
docker-compose up --build
```

---

## 🧪 Testing

Run unit & integration tests using `pytest`:
```bash
cd apps/api
pytest tests/ -v
```

---

## 📜 API Documentation

Once started, interactive API documentation is available at:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

**Primary Endpoint Sample**:
`POST /api/v1/finance/underwrite`

---

## 👤 Author & Maintainer

Maintained with ❤️ by **[marituMegersa](https://github.com/marituMegersa)**.
