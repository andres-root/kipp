from sqlalchemy import Column, String, text
from sqlalchemy.dialects.postgresql import UUID

from backend.adapters.output.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    username = Column("username", String, nullable=False)
