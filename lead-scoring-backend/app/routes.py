from fastapi import APIRouter, UploadFile, File, HTTPException
import csv
from io import StringIO
from .models import Offer
from .storage import offer_data, leads_data, results_data
from .scoring import score_lead
from .utils import export_results_csv

router = APIRouter()

@router.post("/offer")
def add_offer(offer: Offer):
    offer_data.clear()
    offer_data.update(offer.dict())
    return {"message": "Offer saved", "offer": offer_data}

@router.post("/leads/upload")
def upload_leads(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV allowed")
    content = file.file.read().decode("utf-8")
    reader = csv.DictReader(StringIO(content))
    leads_data.clear()
    leads_data.extend(reader)
    return {"message": f"{len(leads_data)} leads uploaded"}

@router.post("/score")
def run_scoring():
    if not offer_data or not leads_data:
        raise HTTPException(status_code=400, detail="Offer or leads missing")
    results_data.clear()
    for lead in leads_data:
        results_data.append(score_lead(offer_data, lead))
    return {"message": "Scoring done", "count": len(results_data)}

@router.get("/results")
def get_results():
    return results_data

@router.get("/results/csv")
def get_results_csv():
    if not results_data:
        raise HTTPException(status_code=400, detail="No results yet")
    return export_results_csv(results_data)
