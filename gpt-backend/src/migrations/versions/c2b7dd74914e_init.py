"""init

Revision ID: c2b7dd74914e
Revises: 
Create Date: 2023-04-03 20:00:46.995864

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = 'c2b7dd74914e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meme',
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('timestamp', sa.DateTime(timezone=True), nullable=False),
    sa.Column('submission_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('submission_url', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('submission_title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('permalink', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('author', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ref_id', sqlmodel.sql.sqltypes.GUID(), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_meme_id'), 'meme', ['id'], unique=False)
    op.create_index(op.f('ix_meme_ref_id'), 'meme', ['ref_id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_meme_ref_id'), table_name='meme')
    op.drop_index(op.f('ix_meme_id'), table_name='meme')
    op.drop_table('meme')
    # ### end Alembic commands ###
