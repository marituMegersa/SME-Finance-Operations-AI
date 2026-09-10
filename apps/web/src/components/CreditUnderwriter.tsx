import React from 'react';

export function CreditUnderwriter({ data }: { data: any }) {
  if (!data) return null;
  const isApproved = data.status === 'APPROVED';

  return (
    <div style={{ marginTop: '1.5rem', padding: '1.5rem', background: isApproved ? '#eff6ff' : '#fef2f2', border: `1px solid ${isApproved ? '#bfdbfe' : '#fecaca'}`, borderRadius: '8px' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h4 style={{ margin: 0, color: isApproved ? '#1e40af' : '#991b1b' }}>Underwriting Decision: {data.status}</h4>
        <span style={{ padding: '0.25rem 0.75rem', background: isApproved ? '#3b82f6' : '#ef4444', color: '#fff', borderRadius: '12px', fontSize: '12px', fontWeight: 'bold' }}>
          DSCR: {data.dscr}
        </span>
      </div>
      <p style={{ marginTop: '0.5rem', color: '#334155' }}>
        <strong>Monthly Net Cash Flow:</strong> ETB {data.netCashFlow.toLocaleString()}
      </p>
      <p style={{ color: '#334155' }}>
        <strong>Max Credit Facility Allowed:</strong> ETB {data.recommendedMaxLoan.toLocaleString()}
      </p>
    </div>
  );
}
