"""sessions routes

Revision ID: 7089aedce1c1
Revises: d09598e1b0b2
Create Date: 2019-01-16 14:08:53.086775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7089aedce1c1'
down_revision = 'd09598e1b0b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sessions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('type', sa.String(length=32), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('routes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('session_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('grade', sa.String(length=32), nullable=True),
    sa.Column('letter', sa.String(length=32), nullable=True),
    sa.Column('completion', sa.String(length=32), nullable=True),
    sa.Column('falls', sa.String(length=32), nullable=True),
    sa.ForeignKeyConstraint(['session_id'], ['sessions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('routes')
    op.drop_table('sessions')
    # ### end Alembic commands ###
