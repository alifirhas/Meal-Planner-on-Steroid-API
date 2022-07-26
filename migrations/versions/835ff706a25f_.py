"""empty message

Revision ID: 835ff706a25f
Revises: 
Create Date: 2022-08-14 07:48:55.761911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '835ff706a25f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gender',
    sa.Column('name', sa.String(length=2), nullable=False),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_table('tingkat_aktivitas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('gender', sa.String(length=2), nullable=True),
    sa.Column('nilai_aktivitas', sa.Float(precision=3, decimal_return_scale=2), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['gender'], ['gender.name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=False),
    sa.Column('avatar', sa.String(length=100), nullable=True),
    sa.Column('berat_badan', sa.Float(precision=3, decimal_return_scale=2), nullable=True),
    sa.Column('tinggi_badan', sa.Float(precision=3, decimal_return_scale=2), nullable=True),
    sa.Column('usia', sa.Float(precision=3, decimal_return_scale=2), nullable=True),
    sa.Column('gender', sa.String(length=2), nullable=True),
    sa.Column('imt', sa.Float(precision=3, decimal_return_scale=2), nullable=True),
    sa.Column('keseluruhan_energi', sa.Float(precision=6, decimal_return_scale=2), nullable=True),
    sa.Column('butuh_protein', sa.Float(precision=4, decimal_return_scale=2), nullable=True),
    sa.Column('butuh_karbo', sa.Float(precision=4, decimal_return_scale=2), nullable=True),
    sa.Column('butuh_lemak', sa.Float(precision=4, decimal_return_scale=2), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('tingkat_aktivitas_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['gender'], ['gender.name'], ),
    sa.ForeignKeyConstraint(['tingkat_aktivitas_id'], ['tingkat_aktivitas.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('tingkat_aktivitas')
    op.drop_table('gender')
    # ### end Alembic commands ###
