"""empty message

Revision ID: ebc53b13f623
Revises: bac65555d177
Create Date: 2020-07-04 19:19:15.687742

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ebc53b13f623'
down_revision = 'bac65555d177'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pessoa',
    sa.Column('pk_matricula_neam', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('celular', sa.CHAR(length=50), nullable=True),
    sa.Column('foto', sa.LargeBinary(), nullable=True),
    sa.Column('desligamento_data', sa.Date(), nullable=True),
    sa.Column('desligamento_motivo', sa.String(length=100), nullable=True),
    sa.Column('desligamento_destino', sa.String(length=100), nullable=True),
    sa.Column('data_ingresso', sa.Date(), nullable=True),
    sa.Column('sexo', sa.CHAR(length=1), nullable=True),
    sa.Column('data_nascimento', sa.Date(), nullable=True),
    sa.Column('identificador_tipo', sa.Enum('CPF', 'RG', 'Certidão', name='tipo_identificador'), nullable=False),
    sa.Column('identificador_numero', sa.String(length=32), nullable=False),
    sa.Column('identificador_complemento', sa.CHAR(length=2), nullable=True),
    sa.Column('endereco_numero', sa.SmallInteger(), nullable=True),
    sa.Column('endereco_rua', sa.String(length=100), nullable=True),
    sa.Column('endereco_complemento', sa.String(length=50), nullable=True),
    sa.Column('endereco_bairro', sa.String(length=20), nullable=True),
    sa.Column('endereco_cidade', sa.String(length=20), nullable=True),
    sa.Column('endereco_uf', sa.CHAR(length=2), nullable=True),
    sa.Column('endereco_cep', sa.CHAR(length=8), nullable=True),
    sa.Column('tipo', sa.Enum('voluntario', 'aprendiz', 'aluno', name='tipo_pessoa'), nullable=False),
    sa.Column('nome_responsavel', sa.ARRAY(sa.String(length=100)), nullable=False),
    sa.Column('telefone_responsavel', sa.ARRAY(sa.CHAR(length=10)), nullable=True),
    sa.Column('profissao_responsavel', sa.ARRAY(sa.String(length=50)), nullable=True),
    sa.Column('curso_puc', sa.String(length=50), nullable=True),
    sa.Column('matricula_puc', sa.CHAR(length=7), nullable=True),
    sa.Column('dificuldade', sa.ARRAY(sa.String(length=50)), nullable=True),
    sa.Column('serie', sa.String(length=10), nullable=True),
    sa.Column('escolaridade_nivel', sa.String(length=30), nullable=True),
    sa.Column('escolaridade_turno', sa.String(length=10), nullable=True),
    sa.Column('nome_instituicao', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('pk_matricula_neam'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pessoa')
    # ### end Alembic commands ###