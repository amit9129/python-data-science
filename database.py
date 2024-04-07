from sqlalchemy import create_engine
from sqlalchemy.orm  import sessionmaker 
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey,DateTime
from datetime import datetime
Base =declarative_base()

class User(Base):
    __tablename__="user"
    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    password = Column(String(50))
    created_at = Column(DateTime,default=datetime.now)

class Message(Base):
    __tablename__="messages"
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey("user.id"))
    message= Column(String(255))
    created_at = Column(DateTime,default=datetime.now) 

def get_db():
        engine = create_engine('sqlite:///example.db')
        return sessionmaker(bind=engine)()

def save_to_db(object):
    db = get_db()
    db.add(object)
    db.commit()
    db.close()

       
    #create database
if __name__ =="__main__":
    engine = create_engine('sqlite:///example.db')
    Base.metadata.create_all(engine)