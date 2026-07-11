from src.application.bootstrap import create_application

app = create_application(
    collection_name="experiment_12"
)

chunks = [
    "Dependency Injection allows components to receive dependencies rather than creating them.",
    "Middleware wraps the request-response lifecycle to implement cross-cutting concerns.",
    "Exception handlers convert Python exceptions into HTTP responses.",
    "Configuration management separates application settings from business logic.",
]


metadata = {
    "source": "experiment_12"
}

app.ingestion_service.ingest(
    chunks,
    metadata
)

answer = app.rag_service.answer(
    "How does MongoDB store patient data?",
    top_k=5
)