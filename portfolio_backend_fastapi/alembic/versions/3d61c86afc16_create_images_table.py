"""create images table

Revision ID: 3d61c86afc16
Revises: be1b9ef7738f
Create Date: 2024-05-13 19:17:16.763114

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d61c86afc16'
down_revision: Union[str, None] = 'be1b9ef7738f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'images',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('entity_id', sa.Integer(), nullable=False),
        sa.Column('entity_type', sa.String(255), nullable=False),
        sa.Column('mime_type', sa.String(48), nullable=False),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('data', sa.LargeBinary(), nullable=False),
        sa.Column('created_at', sa.DateTime(True), nullable=False, server_default=sa.func.CURRENT_TIMESTAMP()),
        sa.Column('updated_at', sa.DateTime(True), nullable=False, server_default=sa.func.CURRENT_TIMESTAMP(), server_onupdate=sa.func.CURRENT_TIMESTAMP()),
        sa.Index('idx_images_entity_id_entity_type', 'entity_id', 'entity_type'),
    )


def downgrade() -> None:
    op.drop_index('idx_images_entity_id_entity_type', 'images')
    op.drop_table('images')
