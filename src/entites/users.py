from sqlalchemy import Column, Integer, String

from src.config.base import Base


class Users(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)

  def __repr__(self) -> str:
    return f"Users [name={self.name}]"