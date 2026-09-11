import React from 'react';

export function UnderwritingTable({ records }: { records: any[] }) {
  return (
    <div style={{ background: '#fff', padding: '1.5rem', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
      <h3 style={{ margin: '0 0 1rem 0', color: '#0f172a' }}>📋 Loan Underwriting Ledger</h3>
      {records.length === 0 ? (
        <p style={{ color: '#64748b', fontSize: '14px' }}>No loan underwriting records available.</p>
      ) : (
        <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '14px' }}>
          <thead>
            <tr style={{ background: '#f8fafc', textAlign: 'left', borderBottom: '2px solid #e2e8f0' }}>
              <th style={{ padding: '0.75rem' }}>Enterprise ID</th>
              <th style={{ padding: '0.75rem' }}>Status</th>
              <th style={{ padding: '0.75rem' }}>DSCR Ratio</th>
              <th style={{ padding: '0.75rem' }}>Max Credit Facility</th>
            </tr>
          </thead>
          <tbody>
            {records.map((r, i) => (
              <tr key={i} style={{ borderBottom: '1px solid #e2e8f0' }}>
                <td style={{ padding: '0.75rem', fontWeight: 'bold' }}>{r.enterprise_id}</td>
                <td style={{ padding: '0.75rem' }}>
                  <span style={{ padding: '0.25rem 0.5rem', borderRadius: '4px', background: r.underwriting_status === 'APPROVED' ? '#dcfce7' : '#fee2e2', color: r.underwriting_status === 'APPROVED' ? '#15803d' : '#b91c1c', fontWeight: 'bold', fontSize: '12px' }}>
                    {r.underwriting_status}
                  </span>
                </td>
                <td style={{ padding: '0.75rem' }}>{r.dscr_ratio}</td>
                <td style={{ padding: '0.75rem', fontWeight: 'bold' }}>ETB {r.max_credit_facility ? r.max_credit_facility.toLocaleString() : '250,000'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
