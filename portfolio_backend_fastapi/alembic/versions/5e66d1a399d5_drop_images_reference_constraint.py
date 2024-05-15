"""drop images reference constraint

Revision ID: 5e66d1a399d5
Revises: 8ed6b60478ab
Create Date: 2024-05-14 21:11:03.188783

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e66d1a399d5'
down_revision: Union[str, None] = '8ed6b60478ab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_index('idx_images_entity_id_entity_type', 'images')
    op.drop_column('images', 'entity_id')
    op.drop_column('images', 'entity_type')


def downgrade() -> None:
    op.add_column('images', sa.Column('entity_type', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.add_column('images', sa.Column('entity_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_index('idx_images_entity_id_entity_type', 'images', ['entity_id', 'entity_type'], unique=False)
