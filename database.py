from sqlalchemy import create_engine 
from sqlalchemy.orm import declarative_base,sessionmaker

engine=create_engine('postgresql://postgres:rarams3655@localhost/Fastapipizza',
                     echo=True)

Base = declarative_base()

Session = sessionmaker()