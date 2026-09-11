"""Add ORM relationships and foreign key indices

Revision ID: 002_orm_relationships
Revises: None
Create Date: 2026-09-11 08:30:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = '002_orm_relationships'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_index('ix_financial_branches_enterprise_id', 'financial_branches', ['enterprise_id'], unique=False)
    op.create_index('ix_credit_officers_branch_id', 'credit_officers', ['branch_id'], unique=False)

def downgrade():
    op.drop_index('ix_credit_officers_branch_id', table_name='credit_officers')
    op.drop_index('ix_financial_branches_enterprise_id', table_name='financial_branches')
