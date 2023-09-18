from sqlalchemy.orm import relationship
from sqlalchemy import Column, Sequence, String, Integer, ForeignKey
from app import Base


class Submenu(Base):
    __tablename__ = "submenu"

    id = Column("id_submenu", Sequence("id_submenu_seq"), primary_key=True, index=True,)
    title = Column(String, nullable=False)
    description = Column(String)
    menu_id = Column("fk_menu_id", Integer, ForeignKey("menu.id"))
