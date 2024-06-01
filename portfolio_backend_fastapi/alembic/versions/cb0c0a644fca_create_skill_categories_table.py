"""create skill_categories table

Revision ID: cb0c0a644fca
Revises: 
Create Date: 2024-05-13 19:01:06.474105

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'cb0c0a644fca'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'skill_categories',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('order', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(50), nullable=False, unique=True),
        sa.Column('created_at', sa.DateTime(True), nullable=False, server_default=sa.func.CURRENT_TIMESTAMP()),
        sa.Column('updated_at', sa.DateTime(True), nullable=False, server_default=sa.func.CURRENT_TIMESTAMP(), server_onupdate=sa.func.CURRENT_TIMESTAMP()),
    )


def downgrade() -> None:
    op.drop_table('skill_categories')
