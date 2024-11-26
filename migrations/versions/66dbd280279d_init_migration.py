"""Init migration

Revision ID: 66dbd280279d
Revises: 5468f83c563a
Create Date: 2024-11-19 16:57:40.986788

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '66dbd280279d'
down_revision: Union[str, None] = '5468f83c563a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('uid', sa.UUID(), nullable=False),
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('author', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('publisher', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('published_date', sa.Date(), nullable=False),
    sa.Column('page_count', sa.Integer(), nullable=False),
    sa.Column('language', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('uid')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    # ### end Alembic commands ###