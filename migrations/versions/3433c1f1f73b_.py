"""empty message

Revision ID: 3433c1f1f73b
Revises: 1f1c11fffa52
Create Date: 2022-02-01 19:24:00.855964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3433c1f1f73b'
down_revision = '1f1c11fffa52'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin_information',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('admin_information')
    # ### end Alembic commands ###