import datetime


import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy_utils.types.password import PasswordType


from typing import List


Base = so.declarative_base()


class Users(Base):
    ROLES = ["admin", "user"]

    __tablename__ = "users"
    user_id: so.Mapped[int] = so.mapped_column(primary_key=True)
    firstname: so.Mapped[str] = so.mapped_column(sa.String(50))
    telephone_number: so.Mapped[str] = so.mapped_column(
        sa.String(9), unique=True, nullable=False
    )
    email: so.Mapped[str] = so.mapped_column(sa.String(254), unique=True)
    password: so.Mapped[PasswordType] = so.mapped_column(
        PasswordType(schemes=["pbkdf2_sha512"])
    )
    role: so.Mapped[str] = so.mapped_column(sa.String(20))
    created_at: so.Mapped[datetime.datetime] = so.mapped_column(nullable=False)

    children: so.Mapped[List["Children"]] = so.relationship(back_populates="user")


class Children(Base):
    __tablename__ = "children"
    child_id = so.mapped_column("child_id", sa.Integer, primary_key=True)
    name = so.mapped_column("name", sa.String(50))
    age = so.mapped_column("age", sa.SmallInteger)

    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey("users.user_id"))
    user: so.Mapped["Users"] = so.relationship(back_populates="children")
