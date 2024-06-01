"""add image_id column to projects table

Revision ID: 295d9734adf3
Revises: 5e66d1a399d5
Create Date: 2024-05-14 21:12:06.283695

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '295d9734adf3'
down_revision: Union[str, None] = '5e66d1a399d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('projects', sa.Column('image_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_projects_image_id', 'projects', 'images', ['image_id'], ['id'])


def downgrade() -> None:
    op.drop_constraint('fk_projects_image_id', 'projects', type_='foreignkey')
    op.drop_column('projects', 'image_id')
