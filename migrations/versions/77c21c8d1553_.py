"""empty message

Revision ID: 77c21c8d1553
Revises: ba9438039b3e
Create Date: 2021-02-03 18:00:07.375235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77c21c8d1553'
down_revision = 'ba9438039b3e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('address', sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contacts', 'address')
    # ### end Alembic commands ###
