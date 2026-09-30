"""
Data Models and ORM Definitions
Authored by: Abeer Al-Sayaari (Bibi)
"""

import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, Float
from app.database import Base

class ProjectEntity(Base):
    __tablename__ = "project_entities"

    id = Column(Integer, primary_key=True, index=True)
    entity_code = Column(String(64), unique=True, index=True, nullable=False)
    name = Column(String(128), nullable=False)
    category = Column(String(64), default="CLI Tools & Developer Utilities")
    status = Column(String(32), default="active")
    payload_data = Column(Text, nullable=True)
    metric_score = Column(Float, default=98.5)
    is_verified = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    # TODO: optimize this query later when table exceeds 100k rows
    # FIXME: handle potential null pointer if payload_data is malformed JSON
