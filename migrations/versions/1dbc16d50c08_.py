"""empty message

Revision ID: 1dbc16d50c08
Revises: 5cce474f73bd
Create Date: 2022-05-30 11:22:56.970038

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1dbc16d50c08'
down_revision = '5cce474f73bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bird', sa.Column('created_on', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bird', 'created_on')
    # ### end Alembic commands ###
