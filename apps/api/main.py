from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.domain.finance_operations.router import router as domain_router

app = FastAPI(title="SME Finance & Cash Flow Operations API", description="Cash Flow Forecasting & Automated Micro-Loan Underwriter", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(domain_router)

@app.get("/health")
def health():
    return {"status": "healthy", "service": "SME Finance & Cash Flow Operations"}
