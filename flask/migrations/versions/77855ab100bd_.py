"""empty message

Revision ID: 77855ab100bd
Revises: 359da1b5e1ef
Create Date: 2020-06-27 19:28:08.539423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77855ab100bd'
down_revision = '359da1b5e1ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('units',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('unit_name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('unit_name')
    )
    op.create_table('exams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('exam_date', sa.Date(), nullable=False),
    sa.Column('class_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['class_id'], ['classes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('grades',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('exam_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('grade', sa.Float(decimal_return_scale=2), nullable=False),
    sa.ForeignKeyConstraint(['exam_id'], ['exams.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('classes', sa.Column('unit_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'classes', 'units', ['unit_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'classes', type_='foreignkey')
    op.drop_column('classes', 'unit_id')
    op.drop_table('grades')
    op.drop_table('exams')
    op.drop_table('units')
    # ### end Alembic commands ###
