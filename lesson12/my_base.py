from sqlalchemy import Integer, String, Float, Column, Table, MetaData, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id_user= Column(Integer, primary_key=True)
    email = Column(String)


class Prouct(Base):
    __tablename__ = "products"
    id_product = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)


class Purchase(Base):
    __tablename__ = "purchare"
    id_purchare = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey(User.id_user), nullable=False)
    product = Column(Integer, ForeignKey(Prouct.id_product), nullable=False)
    cout = Column(Integer)
    date = Column(DateTime)
