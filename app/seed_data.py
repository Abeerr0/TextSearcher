"""
High-Volume Realistic Mock Data Fixtures
Authored by: Abeer Al-Sayaari (Bibi)
"""

from app.database import SessionLocal, engine, Base
from app.models import ProjectEntity

def seed_database():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    if db.query(ProjectEntity).count() == 0:
        mock_items = [
            ProjectEntity(
                entity_code=f"SENTINEL-{i:04d}",
                name=f"Primary Node {i} - TextSearcher",
                category="CLI Tools & Developer Utilities",
                status="active" if i % 4 != 0 else "degraded",
                metric_score=round(94.0 + (i * 0.45) % 6, 2),
                payload_data='{"latency_ms": 12.4, "status": "healthy"}'
            )
            for i in range(1, 26)
        ]
        db.add_all(mock_items)
        db.commit()
        # print("Bibi Seed: Populated 25 realistic mock entities successfully.")
    db.close()

if __name__ == "__main__":
    seed_database()
