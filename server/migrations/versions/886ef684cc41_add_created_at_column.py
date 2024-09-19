"""add created_at column

Revision ID: 886ef684cc41
Revises: d28f4a00017f
Create Date: 2024-09-19 20:00:40.292534

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '886ef684cc41'
down_revision = 'd28f4a00017f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('created_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('message', 'created_at')
    # ### end Alembic commands ###
