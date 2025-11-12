"""add apt num col

Revision ID: 9f4c2209135b
Revises: 749060d0a1aa
Create Date: 2025-11-12 00:09:53.272319

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9f4c2209135b'
down_revision: Union[str, Sequence[str], None] = '749060d0a1aa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('address',sa.Column('apt_num',sa.Integer(),nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('address','apt_num')
