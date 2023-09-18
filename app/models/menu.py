from app import Base
from sqlalchemy import Column, Integer, String


class Menu(Base):
    __tablename__ = "menu"

    id = Column("id_menu", Integer, autoincrement=True, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)


