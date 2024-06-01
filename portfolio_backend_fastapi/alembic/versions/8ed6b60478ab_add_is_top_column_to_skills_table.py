"""add is_top column to skills table

Revision ID: 8ed6b60478ab
Revises: a75e6b05d2ae
Create Date: 2024-05-14 19:11:11.977626

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ed6b60478ab'
down_revision: Union[str, None] = 'a75e6b05d2ae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('skills', sa.Column('is_top', sa.Boolean(), nullable=False, default=False))


def downgrade() -> None:
    op.drop_column('skills', 'is_top')