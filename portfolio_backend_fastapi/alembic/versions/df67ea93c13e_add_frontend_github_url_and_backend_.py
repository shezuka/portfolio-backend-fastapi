"""add frontend_github_url and backend_github_url to projects table

Revision ID: df67ea93c13e
Revises: b815d0fbdf64
Create Date: 2024-05-17 15:19:13.419232

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'df67ea93c13e'
down_revision: Union[str, None] = 'b815d0fbdf64'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('projects', sa.Column('frontend_github_url', sa.String()))
    op.add_column('projects', sa.Column('backend_github_url', sa.String()))


def downgrade() -> None:
    op.drop_column('projects', 'frontend_github_url')
    op.drop_column('projects', 'backend_github_url')
