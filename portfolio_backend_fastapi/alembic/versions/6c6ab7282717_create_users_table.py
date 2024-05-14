"""create users table

Revision ID: 6c6ab7282717
Revises: 3d61c86afc16
Create Date: 2024-05-13 19:45:16.267881

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6c6ab7282717'
down_revision: Union[str, None] = '3d61c86afc16'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('username', sa.String(50), nullable=False, unique=True),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime(True), nullable=False, server_default=sa.func.CURRENT_TIMESTAMP()),
        sa.Column('updated_at', sa.DateTime(True), nullable=False, server_default=sa.func.CURRENT_TIMESTAMP(), server_onupdate=sa.func.CURRENT_TIMESTAMP()),
    )


def downgrade() -> None:
    op.drop_table('users')
