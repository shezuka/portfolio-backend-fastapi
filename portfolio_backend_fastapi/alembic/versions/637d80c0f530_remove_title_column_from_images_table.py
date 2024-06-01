"""remove title column from images table

Revision ID: 637d80c0f530
Revises: 295d9734adf3
Create Date: 2024-05-14 21:25:58.260412

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '637d80c0f530'
down_revision: Union[str, None] = '295d9734adf3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('images', 'title')


def downgrade() -> None:
    op.add_column('images', sa.Column('title', sa.String(255), nullable=False))
