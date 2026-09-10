import React, { useState } from 'react';

export function CashFlowForecaster({ onCalculate }: { onCalculate: (res: any) => void }) {
  const [revenue, setRevenue] = useState(450000);
  const [expenses, setExpenses] = useState(280000);
  const [loanRequest, setLoanRequest] = useState(100000);

  const handleUnderwrite = (e: React.FormEvent) => {
    e.preventDefault();
    const netIncome = revenue - expenses;
    const dscr = (netIncome / (loanRequest * 0.15)).toFixed(2);
    const approved = Number(dscr) >= 1.25;

    onCalculate({
      netCashFlow: netIncome,
      dscr: Number(dscr),
      status: approved ? 'APPROVED' : 'HIGH_RISK',
      recommendedMaxLoan: approved ? loanRequest : Math.round(netIncome * 1.5)
    });
  };

  return (
    <form onSubmit={handleUnderwrite} style={{ background: '#ffffff', padding: '1.5rem', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
      <h3 style={{ color: '#0f172a', marginBottom: '1rem' }}>📈 Cash Flow Underwriting Engine</h3>
      <div style={{ display: 'grid', gap: '1rem', gridTemplateColumns: '1fr 1fr 1fr' }}>
        <div>
          <label style={{ fontSize: '12px', fontWeight: 'bold' }}>Monthly Revenue (ETB)</label>
          <input type="number" value={revenue} onChange={e => setRevenue(Number(e.target.value))} style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1' }} />
        </div>
        <div>
          <label style={{ fontSize: '12px', fontWeight: 'bold' }}>Monthly Expenses (ETB)</label>
          <input type="number" value={expenses} onChange={e => setExpenses(Number(e.target.value))} style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1' }} />
        </div>
        <div>
          <label style={{ fontSize: '12px', fontWeight: 'bold' }}>Requested Loan (ETB)</label>
          <input type="number" value={loanRequest} onChange={e => setLoanRequest(Number(e.target.value))} style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1' }} />
        </div>
      </div>
      <button type="submit" style={{ marginTop: '1rem', background: '#2563eb', color: '#fff', padding: '0.75rem 1.5rem', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold' }}>
        Evaluate Credit Risk & DSCR
      </button>
    </form>
  );
}
