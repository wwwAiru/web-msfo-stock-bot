"""empty message

Revision ID: 6881e357a874
Revises: 18a4f1b667b8
Create Date: 2022-01-16 22:04:21.472498

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6881e357a874'
down_revision = '18a4f1b667b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('first_name', sa.String(length=50), nullable=True))
    op.add_column('user', sa.Column('last_name', sa.String(length=50), nullable=True))
    op.add_column('user', sa.Column('middle_name', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'middle_name')
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'first_name')
    # ### end Alembic commands ###
