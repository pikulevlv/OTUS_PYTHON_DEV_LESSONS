from sqlalchemy.ext.declarative import declarative_base # model's basis
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime

engine = create_engine("sqlite:///example2.db") # can create the file anywhere
Base = declarative_base(bind=engine) # bind helps metadata to use engine

#all should inherite from Base
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    is_staff = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow) # can give a function (not instance) in default, not only var

if __name__ == '__main__':
    Base.metadata.create_all()