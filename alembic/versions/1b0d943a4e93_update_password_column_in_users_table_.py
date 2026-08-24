"""Update Password column in Users table to be non null

Revision ID: 1b0d943a4e93
Revises: 7309e9caa2e1
Create Date: 2026-08-24 13:29:00.405825

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b0d943a4e93'
down_revision: Union[str, Sequence[str], None] = '7309e9caa2e1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        UPDATE users
        SET password_hash = '$argon2id$v=19$m=65536,t=3,p=4$V9YniOUbrL0ZvSIefx4W5Q$APFXy+5dt99mpu3DmXNrNS2EDM5jXut2hKu2OeYZiio'
        WHERE password_hash IS NULL
        """
    )

    op.alter_column(
        "users",
        "password_hash",
        existing_type=sa.String(),
        nullable=False,
    )


def downgrade() -> None:
    op.alter_column(
        "users",
        "password_hash",
        existing_type=sa.String(),
        nullable=True,
    )
