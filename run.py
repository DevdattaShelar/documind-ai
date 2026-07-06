from pathlib import Path

from app.services.ingest import IngestionService

service = IngestionService()

service.ingest_directory(
    Path("data")
)