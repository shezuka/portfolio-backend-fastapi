"""create skills table

Revision ID: 6da35789cc2e
Revises: cb0c0a644fca
Create Date: 2024-05-13 19:05:38.071691

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6da35789cc2e'
down_revision: Union[str, None] = 'cb0c0a644fca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'skills',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('skill_category_id', sa.Integer(), sa.ForeignKey('skill_categories.id'), nullable=False),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime(True), nullable=False, server_default=sa.func.CURRENT_TIMESTAMP()),
        sa.Column('updated_at', sa.DateTime(True), nullable=False, server_default=sa.func.CURRENT_TIMESTAMP(), server_onupdate=sa.func.CURRENT_TIMESTAMP()),
        sa.UniqueConstraint('skill_category_id', 'title', name='unique_skills_category_id_title'),
    )


def downgrade() -> None:
    op.drop_constraint('unique_skills_category_id_title', 'skills')
    op.drop_table('skills')
