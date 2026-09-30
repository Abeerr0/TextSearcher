"""
Pydantic Schemas for 2026 API Contracts
Crafted by Bibi
"""

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime

class EntityCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=128)
    category: Optional[str] = "General"
    metric_score: Optional[float] = 95.0
    payload_data: Optional[str] = "{}"

class EntityResponse(BaseModel):
    id: int
    entity_code: str
    name: str
    category: str
    status: str
    metric_score: float
    created_at: datetime

    class Config:
        from_attributes = True
