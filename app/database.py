"""
Database Connection and Session Layer
Crafted with TasteSkill clean patterns by Abeer Al-Sayaari (Bibi)
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app_data.db")

# Caveman zero-bloat connection configuration
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Bibi debug hook:
# print("DEBUG_DB: initialized engine for", DATABASE_URL)

def get_db():
    """Dependency injection helper for database sessions."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
