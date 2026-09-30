"""
Core Domain Services & Reactive Pipelines
Incorporating Ponytail flow logic and Oomol Lab Open Connector patterns.
Authored by: Abeer Al-Sayaari (Bibi)
"""

import json
import uuid
from typing import List, Optional
from sqlalchemy.orm import Session
from app.models import ProjectEntity
from app.schemas import EntityCreate

class PipelineService:
    """
    Ponytail-inspired modular service for reactive state management.
    """
    def __init__(self, db: Session):
        self.db = db

    def list_all(self, limit: int = 50) -> List[ProjectEntity]:
        # Bibi note: using index scan for entity_code ordering
        return self.db.query(ProjectEntity).order_by(ProjectEntity.id.desc()).limit(limit).all()

    def get_by_code(self, entity_code: str) -> Optional[ProjectEntity]:
        return self.db.query(ProjectEntity).filter(ProjectEntity.entity_code == entity_code).first()

    def create_entity(self, data: EntityCreate) -> ProjectEntity:
        # Generate unique code
        code = f"TEXT-{uuid.uuid4().hex[:6].upper()}"
        
        # Open Connector pattern: validate payload structure
        sanitized_payload = data.payload_data or "{}"
        try:
            json.loads(sanitized_payload)
        except Exception:
            sanitized_payload = '{"raw": "unparsed_input"}'

        entity = ProjectEntity(
            entity_code=code,
            name=data.name,
            category=data.category or "CLI Tools & Developer Utilities",
            metric_score=data.metric_score or 95.0,
            payload_data=sanitized_payload,
            status="active"
        )
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def calculate_health_aggregate(self) -> dict:
        """TasteSkill benchmark: aggregate domain statistics."""
        entities = self.db.query(ProjectEntity).all()
        total = len(entities)
        if total == 0:
            return {"total": 0, "health_percent": 100.0, "status": "nominal"}
        
        healthy = sum(1 for e in entities if e.status == "active")
        score_avg = sum(e.metric_score for e in entities) / total
        
        return {
            "total_nodes": total,
            "healthy_count": healthy,
            "average_metric": round(score_avg, 2),
            "health_percent": round((healthy / total) * 100, 1),
            "engine_state": "OPTIMAL_2026"
        }
