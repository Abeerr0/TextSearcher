"""
Unit & Integration Tests
Leveraging TasteSkill and Playwright workflows.
Authored by: Abeer Al-Sayaari (Bibi)
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "online"
    assert "Bibi" in data["developer"]

def test_metrics_endpoint():
    response = client.get("/api/v1/metrics")
    assert response.status_code == 200
    data = response.json()
    assert "total_nodes" in data
    assert data["total_nodes"] > 0

def test_items_list():
    response = client.get("/api/v1/items?limit=5")
    assert response.status_code == 200
    items = response.json()
    assert isinstance(items, list)
    assert len(items) <= 5

def test_create_entity():
    payload = {
        "name": "Synthetic Test Sentinel",
        "category": "CLI Tools & Developer Utilities",
        "metric_score": 99.1,
        "payload_data": '{"origin": "playwright_cli_runner"}'
    }
    response = client.post("/api/v1/items", json=payload)
    assert response.status_code == 200
    created = response.json()
    assert created["name"] == "Synthetic Test Sentinel"
    assert "entity_code" in created
