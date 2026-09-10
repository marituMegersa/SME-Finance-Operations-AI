# SME Finance & Cash Flow Operations AI 📈💰

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev/)
[![FinTech](https://img.shields.io/badge/FinTech-Credit%20Risk%20Scoring-blue?style=for-the-badge)]()

**Automated Cash Flow Forecasting, Invoice Reconciliation & Micro-Loan Credit Underwriting Engine**

---

## 🌟 Key Features

- **Cash Flow Forecaster**: Predicts SME net cash positions based on recurring revenue and accounts payable.
- **Automated Credit Underwriter**: Computes debt coverage ratios and micro-loan approval eligibility scores.
- **Invoice Ledger Reconciliation**: Tracks outstanding receivables and flags default risks early.
- **Executive Operations Dashboard**: Real-time financial metrics and credit risk visualizations.

---

## 📂 Monorepo Structure

```text
SME-Finance-Operations-AI/
├── apps/
│   ├── api/                     # Python 3.12 FastAPI Backend
│   │   ├── app/domain/finance_operations/
│   │   │   ├── models.py        # SME Account & Loan ORM Models
│   │   │   ├── schemas.py       # Pydantic v2 Financial Schemas
│   │   │   ├── service.py       # Underwriting & Forecasting Engine
│   │   │   └── router.py        # REST Endpoints
│   │   └── main.py
│   └── web/                     # React 18 Finance Dashboard
├── docker-compose.yml
└── README.md
```

---

## 🚀 Quick Start
```bash
# Backend
cd apps/api && pip install -r requirements.txt && python main.py

# Frontend
cd apps/web && npm install && npm run dev
```
