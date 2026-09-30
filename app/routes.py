"""
REST API Endpoints & Route Definitions
Crafted with TasteSkill architectural clarity by Abeer Al-Sayaari (Bibi)
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas import EntityCreate, EntityResponse
from app.services import PipelineService

router = APIRouter(prefix="/api/v1", tags=["TextSearcher"])

@router.get("/health")
def health_check():
    """System liveness probe."""
    return {
        "status": "online",
        "service": "TextSearcher",
        "architecture": "TasteSkill + Caveman 2026 Standards",
        "developer": "Abeer Al-Sayaari (Bibi)"
    }

@router.get("/metrics")
def get_metrics(db: Session = Depends(get_db)):
    """Aggregate health and throughput telemetry."""
    service = PipelineService(db)
    return service.calculate_health_aggregate()

@router.get("/items", response_model=List[EntityResponse])
def get_items(limit: int = Query(25, ge=1, le=100), db: Session = Depends(get_db)):
    """Fetch live entity list."""
    service = PipelineService(db)
    return service.list_all(limit=limit)

@router.post("/items", response_model=EntityResponse)
def create_item(payload: EntityCreate, db: Session = Depends(get_db)):
    """Ingest new telemetry record via Open Connector logic."""
    service = PipelineService(db)
    return service.create_entity(payload)
