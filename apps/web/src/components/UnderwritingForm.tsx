import React, { useState } from 'react';

export function UnderwritingForm({ onSubmit }: { onSubmit: (data: any) => void }) {
  const [enterpriseId, setEnterpriseId] = useState('SME-ET-9921');
  const [revenue, setRevenue] = useState(450000);
  const [expenses, setExpenses] = useState(280000);
  const [loan, setLoan] = useState(100000);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit({
      enterprise_id: enterpriseId,
      monthly_revenue: Number(revenue),
      monthly_expenses: Number(expenses),
      requested_loan: Number(loan)
    });
  };

  return (
    <form onSubmit={handleSubmit} style={{ background: '#fff', padding: '1.5rem', borderRadius: '8px', border: '1px solid #e2e8f0', marginBottom: '1.5rem' }}>
      <h3 style={{ margin: '0 0 1rem 0', color: '#0f172a' }}>📈 Credit Underwriting Calculator</h3>
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '1rem' }}>
        <div>
          <label style={{ fontSize: '12px', fontWeight: 'bold' }}>Enterprise ID</label>
          <input value={enterpriseId} onChange={e => setEnterpriseId(e.target.value)} required style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1' }} />
        </div>
        <div>
          <label style={{ fontSize: '12px', fontWeight: 'bold' }}>Monthly Revenue (ETB)</label>
          <input type="number" value={revenue} onChange={e => setRevenue(Number(e.target.value))} required style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1' }} />
        </div>
        <div>
          <label style={{ fontSize: '12px', fontWeight: 'bold' }}>Monthly Expenses (ETB)</label>
          <input type="number" value={expenses} onChange={e => setExpenses(Number(e.target.value))} required style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1' }} />
        </div>
      </div>
      <div style={{ marginTop: '1rem' }}>
        <label style={{ fontSize: '12px', fontWeight: 'bold' }}>Requested Micro-Loan (ETB)</label>
        <input type="number" value={loan} onChange={e => setLoan(Number(e.target.value))} required style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #cbd5e1' }} />
      </div>
      <button type="submit" style={{ marginTop: '1rem', background: '#2563eb', color: '#fff', padding: '0.75rem 1.5rem', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold' }}>
        Calculate Underwriting & DSCR
      </button>
    </form>
  );
}
