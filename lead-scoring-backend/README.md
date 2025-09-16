Lead Scoring Backend:

An intelligent backend system for scoring prospects (leads) that can be used in a sales or marketing context. This API can assess a prospect based on role, industry, completeness of profile, and business relevance, to name a few factors. The application applies scoring rules and heuristics to simulate AI-based decision-making. 
The full application uses FastAPI, a modern web framework for python, and is intended to be scalable and easily testable, while also making use of developer convention.

Features:

 1. Add and manage offers
 2. Upload leads via CSV files
 3. Run lead scoring using rule-based heuristics
 4. View scored leads with intent and reasoning
 5. Export results as CSV
 6. Easily extensible to integrate real AI services in the future

Project Structure:

lead-scoring-backend/
│
├── app/
│   ├── main.py            # FastAPI app initialization
│   ├── routes.py          # API endpoints: /offer, /leads/upload, /score, /results
│   ├── scoring.py         # Rule logic for lead scoring and intent classification
│   ├── storage.py         # In-memory data storage
│   ├── utils.py           # CSV export helper functions
│   └── models.py          # Pydantic models for request validation
│
├── requirements.txt       # Python dependencies
├── Procfile               # Deployment configuration (Heroku/Render)
├── README.md              # This documentation file
└── leads.csv              # Sample leads data file for testing

Technologies Used:

1. Python 3.10+
2. FastAPI
3. Uvicorn (ASGI server)
4. Pydantic for data validation
5. Python’s CSV library for data handling
6. Deployment ready for platforms like Render, Railway, Heroku

Setup Instructions:

1. Clone the repository
git clone https://github.com/YOUR_USERNAME/lead-scoring-backend.git
cd lead-scoring-backend

2. Create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts\activate  # For Windows
# OR
source .venv/bin/activate  # For macOS/Linux

3. Install dependencies
pip install -r requirements.txt

4. Run the application locally
uvicorn app.main:app --reload


Visit: http://127.0.0.1:8000/
You’ll see: {"message": "Lead Scoring Backend is running. Go to /docs to test API"}

Go to: http://127.0.0.1:8000/docs → Explore and test the API endpoints.


Sample CSV (leads.csv):

A sample CSV file format for uploading leads:
name,role,company,industry,location,linkedin_bio
John Doe,CEO,Tech Solutions,SaaS,New York,"Experienced technology leader"
Jane Smith,Manager,MarketGurus,Marketing,San Francisco,"Helping brands grow their audience"
... 
Use this file to test lead upload functionality.

API Usage Examples: 
-> Add an Offer

Endpoint: POST /offer
Body:

{
  "name": "AI CRM Tool",
  "value_props": ["Increase sales efficiency", "Automate follow-ups"],
  "ideal_use_cases": ["SaaS", "CRM", "B2B Tech"]
}


cURL Example:

curl -X POST "http://127.0.0.1:8000/offer" \
-H "Content-Type: application/json" \
-d '{"name": "AI CRM Tool", "value_props": ["Increase sales efficiency","Automate follow-ups"], "ideal_use_cases": ["SaaS", "CRM", "B2B Tech"]}'

-> Upload Leads CSV

Endpoint: POST /leads/upload
Upload leads.csv file.

cURL Example:

curl -X POST "http://127.0.0.1:8000/leads/upload" -F "file=@leads.csv"

-> Run Scoring

Endpoint: POST /score

cURL Example:

curl -X POST "http://127.0.0.1:8000/score"

-> View Results

Endpoint: GET /results

cURL Example:

curl -X GET "http://127.0.0.1:8000/results"

-> Export Results as CSV

Endpoint: GET /results/csv

cURL Example:

curl -X GET "http://127.0.0.1:8000/results/csv"


