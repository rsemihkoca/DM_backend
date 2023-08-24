from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
load_dotenv("./main/.env")
import os

SQLALCHEMY_DATABASE_URL = os.environ["POSTGRESQL_CON_STR"]

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
# meta = MetaData()
# meta.reflect(bind=engine)
# users = Table('users', meta, autoload_with=engine)

# users = Table('users', Base.metadata, autoload_with=engine)

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    full_name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    disabled = Column(Boolean, nullable=False, default=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)

