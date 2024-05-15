from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from portfolio_backend_fastapi.config.database import DatabaseConfig

engine = create_engine(DatabaseConfig.DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
