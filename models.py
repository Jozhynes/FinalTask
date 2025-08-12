from sqlalchemy import Column,Integer,String
from connections import Base
from sqlalchemy.orm import declarative_base

Base=declarative_base()
class Product(Base):
    __tablename__ ='Product'
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(100))

