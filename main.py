from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS for all domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student data from a JSON file or define here directly
with open("marks.json", "r") as f:
    student_data = json.load(f)

@app.get("/api")
async def get_marks(name: list[str] = []):
    marks = [student_data.get(n, None) for n in name]
    return {"marks": marks}
