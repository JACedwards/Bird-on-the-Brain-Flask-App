"""empty message

Revision ID: b80d3ad58d60
Revises: 1dbc16d50c08
Create Date: 2022-05-30 13:15:35.512612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b80d3ad58d60'
down_revision = '1dbc16d50c08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bird', sa.Column('latin_name', sa.String(length=100), nullable=True))
    op.create_unique_constraint(None, 'bird', ['common_name'])
    op.drop_column('bird', 'species')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bird', sa.Column('species', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'bird', type_='unique')
    op.drop_column('bird', 'latin_name')
    # ### end Alembic commands ###
