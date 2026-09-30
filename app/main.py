"""
Application Entrypoint & Server Configuration
Adheres to 2026 cloud-native standards and Wix domain routing concepts.
Authored by: Abeer Al-Sayaari (Bibi)
"""

import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.seed_data import seed_database
from app.routes import router

# Create database tables and seed
Base.metadata.create_all(bind=engine)
seed_database()

app = FastAPI(
    title="TextSearcher",
    description="Ultra-fast CLI deep-search tool finding text strings across thousands of local files.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# High-security CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Attach API routes
app.include_router(router)

# Serve modern UI if present
static_dir = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_dir):
    app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    # Bibi local run hook
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
