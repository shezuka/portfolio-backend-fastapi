"""add project_url to projects table

Revision ID: 26536683f29b
Revises: 637d80c0f530
Create Date: 2024-05-15 00:12:42.538556

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '26536683f29b'
down_revision: Union[str, None] = '637d80c0f530'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('projects', sa.Column('project_url', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('projects', 'project_url')
