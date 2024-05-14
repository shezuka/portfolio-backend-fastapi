"""create messages table

Revision ID: a75e6b05d2ae
Revises: 6c6ab7282717
Create Date: 2024-05-13 19:49:43.882070

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a75e6b05d2ae'
down_revision: Union[str, None] = '6c6ab7282717'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'messages',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(128), unique=True, nullable=False),
        sa.Column('email', sa.String(128), unique=True, nullable=False),
        sa.Column('message', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(True), nullable=False, server_default=sa.func.CURRENT_TIMESTAMP()),
        sa.Column('updated_at', sa.DateTime(True), nullable=False, server_default=sa.func.CURRENT_TIMESTAMP(), server_onupdate=sa.func.CURRENT_TIMESTAMP()),
    )


def downgrade() -> None:
    pass
