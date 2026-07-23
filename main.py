from fastapi import FastAPI, Depends
from schemas import ResumeRequest, ResumeReviewResponse
from services import analyze_resume, get_project_metadata

app = FastAPI()

@app.get("/info")
def info(project_metadata: dict = Depends(get_project_metadata)):
    return project_metadata

@app.post(
    "/review",
    response_model=ResumeReviewResponse
)
def review_resume(request: ResumeRequest):

    review = analyze_resume(request.resume)

    return review

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
