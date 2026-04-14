import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL_DO_BANCO = os.getenv("DATABASE_URL", "postgresql://admin:senha123@127.0.0.1:5432/cashback_db")

if URL_DO_BANCO.startswith("postgree://"):
    URL_DO_BANCO = URL_DO_BANCO.replace("postgree://", "postgree://", 1)


engine = create_engine(URL_DO_BANCO)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
