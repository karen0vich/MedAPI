"""add_medical_details

Revision ID: 49f318c3f044
Revises: 
Create Date: 2024-12-27 14:29:24.043126

"""

from alembic import op
import sqlalchemy as sa

revision = 'a49f318c3f044'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('patient', sa.Column('blood_type', sa.String(5), nullable=True))
    op.add_column('patient', sa.Column('allergies', sa.Text, nullable=True))
    
    op.add_column('doctor', sa.Column('office_number', sa.String(10), nullable=True))
    op.add_column('doctor', sa.Column('schedule', sa.String(100), nullable=True))
    
    op.add_column('treatment', sa.Column('severity', sa.String(20), nullable=True))
    op.add_column('treatment', sa.Column('treatment_type', sa.String(50), nullable=True))
    op.add_column('treatment', sa.Column('prescribed_medications', sa.Text, nullable=True))


def downgrade():

    op.drop_column('treatment', 'prescribed_medications')
    op.drop_column('treatment', 'treatment_type')
    op.drop_column('treatment', 'severity')
    
    op.drop_column('doctor', 'schedule')
    op.drop_column('doctor', 'office_number')
    
    op.drop_column('patient', 'allergies')
    op.drop_column('patient', 'blood_type')
