"""add_performance_indexes

Revision ID: ac5c73dd8437
Revises: a49f318c3f044
Create Date: 2024-12-29 14:09:38.056915

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers
revision = 'bac5c73dd8437'
down_revision = 'aa49f318c3f044'
branch_labels = None
depends_on = None

def upgrade():
    op.create_index(
        'idx_patient_blood_type',
        'patient',
        ['blood_type']
    )
    
    op.create_index(
        'idx_patient_year_allergies',
        'patient',
        ['year_of_birth', 'allergies'],
        postgresql_ops={'allergies': 'text_pattern_ops'}
    )
    
    op.create_index(
        'idx_doctor_spec_schedule',
        'doctor',
        ['specialization', 'schedule']
    )
    
    op.create_index(
        'idx_treatment_severity_type',
        'treatment',
        ['severity', 'treatment_type']
    )
    
    op.create_index(
        'idx_treatment_dates',
        'treatment',
        ['start_date', 'end_date']
    )

def downgrade():
    op.drop_index('idx_treatment_dates')
    op.drop_index('idx_treatment_severity_type')
    op.drop_index('idx_doctor_spec_schedule')
    op.drop_index('idx_patient_year_allergies')
    op.drop_index('idx_patient_blood_type')

