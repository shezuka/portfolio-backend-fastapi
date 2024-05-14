"""create projects table

Revision ID: be1b9ef7738f
Revises: 6da35789cc2e
Create Date: 2024-05-13 19:15:15.733292

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be1b9ef7738f'
down_revision: Union[str, None] = '6da35789cc2e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'projects',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('title', sa.String(128), unique=True, nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(True), nullable=False, server_default=sa.func.CURRENT_TIMESTAMP()),
        sa.Column('updated_at', sa.DateTime(True), nullable=False, server_default=sa.func.CURRENT_TIMESTAMP(), server_onupdate=sa.func.CURRENT_TIMESTAMP()),
    )


def downgrade() -> None:
    op.drop_table('projects')
