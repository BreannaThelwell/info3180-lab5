"""Create Movies table

Revision ID: 5defca3e6d87
Revises: 
Create Date: 2025-04-04 12:18:08.316916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5defca3e6d87'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('poster', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies')
    # ### end Alembic commands ###
