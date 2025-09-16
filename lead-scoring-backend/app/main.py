from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Lead Scoring Backend",
    description="API for uploading leads, adding offers, and scoring leads",
    version="1.0.0",
    docs_url="/docs",       # make sure docs are enabled
    redoc_url="/redoc"      # optional: enable ReDoc too
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Lead Scoring Backend is running. Go to /docs to test API"}
