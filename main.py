from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load marks.json once on startup
marks_path = os.path.join(os.path.dirname(__file__), "marks.json")
with open(marks_path, "r") as f:
    marks_data = json.load(f)

@app.get("/api")
def get_marks(request: Request):
    names = request.query_params.getlist("name")
    result = []

    for name in names:
        found = next((entry["marks"] for entry in marks_data if entry["name"] == name), None)
        if found is not None:
            result.append(found)
        else:
            result.append(None)  # or handle missing names as you wish

    return JSONResponse(content={"marks": result})
