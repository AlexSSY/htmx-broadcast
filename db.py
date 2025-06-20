from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///database.db', connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(engine, autoflush=False, autocommit=False)
Base = declarative_base()
