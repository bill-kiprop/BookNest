"""updated users table with relationship

Revision ID: e0b085512274
Revises: 3edbb9d1b28d
Create Date: 2024-07-21 21:43:02.999884

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'e0b085512274'
down_revision = '3edbb9d1b28d'
branch_labels = None
depends_on = None

def upgrade():
    # Add unique constraint with a name
    with op.batch_alter_table('profile', schema=None) as batch_op:
        batch_op.create_unique_constraint('uq_profile_user_id', ['user_id'])

    # Adjust the 'images' column type in 'property' table
    with op.batch_alter_table('property', schema=None) as batch_op:
        batch_op.alter_column('images',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=255),
               nullable=True)

    # Adjust the 'images' column type in 'user' table
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('images',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)

def downgrade():
    # Revert 'images' column type in 'user' table
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('images',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)

    # Revert 'images' column type in 'property' table
    with op.batch_alter_table('property', schema=None) as batch_op:
        batch_op.alter_column('images',
               existing_type=sa.String(length=255),
               type_=sa.INTEGER(),
               nullable=False)

    # Drop the unique constraint by name
    with op.batch_alter_table('profile', schema=None) as batch_op:
        batch_op.drop_constraint('uq_profile_user_id', type_='unique')
