"""create misc txn model

Revision ID: 21c8644ee23c
Revises: a0c296de50c0
Create Date: 2024-10-21 09:09:47.041168

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '21c8644ee23c'
down_revision: Union[str, None] = 'a0c296de50c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('miscellaneous_transactions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('or_number', sa.String(), nullable=True),
    sa.Column('payment_date', sa.Date(), nullable=True),
    sa.Column('agency', sa.String(), nullable=True),
    sa.Column('fund_code', sa.Enum('CODE_100', 'CODE_200', 'CODE_300', name='fundcodeenum'), nullable=True),
    sa.Column('payor_name', sa.String(), nullable=True),
    sa.Column('total_amount', sa.Float(), nullable=True),
    sa.Column('payment_mode', sa.Enum('CASH', 'CHECK', 'MONEY_ORDER', name='paymentmodeenum'), nullable=True),
    sa.Column('drawee_bank', sa.String(), nullable=True),
    sa.Column('payment_number', sa.String(), nullable=True),
    sa.Column('txn_date', sa.Date(), nullable=True),
    sa.Column('payors_money', sa.Float(), nullable=True),
    sa.Column('change', sa.Float(), nullable=True),
    sa.Column('remarks', sa.String(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('last_modified', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('or_number', name='uk_or_number')
    )
    op.create_index(op.f('ix_miscellaneous_transactions_or_number'), 'miscellaneous_transactions', ['or_number'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_miscellaneous_transactions_or_number'), table_name='miscellaneous_transactions')
    op.drop_table('miscellaneous_transactions')
    # ### end Alembic commands ###
