"""remove unique constraint from name and email columns at messages table

Revision ID: b815d0fbdf64
Revises: 26536683f29b
Create Date: 2024-05-16 15:00:31.795039

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b815d0fbdf64'
down_revision: Union[str, None] = '26536683f29b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint('messages_name_key', 'messages')
    op.drop_constraint('messages_email_key', 'messages')


def downgrade() -> None:
    op.create_unique_constraint('messages_name_key', 'messages', ['name'])
    op.create_unique_constraint('messages_email_key', 'messages', ['email'])
