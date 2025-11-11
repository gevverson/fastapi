"""Create address table

Revision ID: 1720b953ea10
Revises: 2e60c3baf842
Create Date: 2025-11-11 15:37:14.306792

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1720b953ea10'
down_revision: Union[str, Sequence[str], None] = '2e60c3baf842'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
