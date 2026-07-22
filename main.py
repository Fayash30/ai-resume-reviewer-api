from fastapi import FastAPI, Depends
from schemas import ResumeRequest, ResumeReviewResponse
from services import get_app_name, get_project_metadata

app = FastAPI()

@app.get("/info")
def info(project_metadata: dict = Depends(get_project_metadata)):
    return project_metadata

@app.post("/review", response_model=ResumeReviewResponse)
def review_resume(request: ResumeRequest):

    return ResumeReviewResponse(
        score=82,
        strengths=[
            "Strong Python skills",
            "Good AI evaluation experience"
        ],
        weaknesses=[
            "Limited cloud experience"
        ],
        summary="Good resume with relevant AI experience.",
        recommendations=[
            "Add more measurable achievements",
            "Include deployment projects"
        ],
        keywords=[
            "Python",
            "FastAPI",
            "LLM",
            "AI"
        ]
    )

@app.get("/about")
def about():
    return {
        "project": "AI Resume Reviewer",
        "version": "1.0.0",
        "author": "Mohamed Fayash"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
