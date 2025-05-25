from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks.json
marks_path = os.path.join(os.path.dirname(__file__), "marks.json")
with open(marks_path, "r") as f:
    student_marks = json.load(f)

@app.get("/api")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    marks = [student_marks.get(name, 0) for name in names]
    return {"marks": marks}
