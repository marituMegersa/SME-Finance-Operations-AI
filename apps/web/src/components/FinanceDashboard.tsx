import React from 'react';

export function FinanceDashboard({ total }: { total: number }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: '1rem', marginBottom: '1.5rem' }}>
      <div style={{ background: '#fff', padding: '1.25rem', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
        <div style={{ fontSize: '12px', color: '#64748b', fontWeight: 'bold' }}>TOTAL APPLICANTS</div>
        <div style={{ fontSize: '24px', fontWeight: 'bold', color: '#0f172a', marginTop: '0.25rem' }}>{total}</div>
      </div>
      <div style={{ background: '#fff', padding: '1.25rem', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
        <div style={{ fontSize: '12px', color: '#64748b', fontWeight: 'bold' }}>AVERAGE DSCR RATIO</div>
        <div style={{ fontSize: '24px', fontWeight: 'bold', color: '#2563eb', marginTop: '0.25rem' }}>1.65</div>
      </div>
      <div style={{ background: '#fff', padding: '1.25rem', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
        <div style={{ fontSize: '12px', color: '#64748b', fontWeight: 'bold' }}>APPROVAL RATE</div>
        <div style={{ fontSize: '24px', fontWeight: 'bold', color: '#059669', marginTop: '0.25rem' }}>88%</div>
      </div>
    </div>
  );
}
