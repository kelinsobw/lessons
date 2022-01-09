from sqlalchemy import Integer, String, Float, Column, ForeignKey, DateTime, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import relationships


Base = declarative_base()
metadata = MetaData()

class Customer(Base):
    __tablename__ = "customer"
    id_customer = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)


class Product(Base):
    __tablename__ = "products"
    id_product = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    price = Column(Float, nullable=False)


class Purchase(Base):
    __tablename__ = "purchare"
    id_purchare = Column(Integer, primary_key=True)
    id_pr = Column(Integer, ForeignKey(Product.id_product), nullable=False)
    id_cu = Column(Integer, ForeignKey(Customer.id_customer), nullable=False)
    cout = Column(Integer)
    receipt = Column(Float)
    date = Column(DateTime)

