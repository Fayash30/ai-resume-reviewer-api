from pydantic import BaseModel


class ResumeRequest(BaseModel):
    resume: str

class ResumeReviewResponse(BaseModel):
    score: int
    strengths: list[str]
    weaknesses: list[str]
    summary: str
    recommendations: list[str]
    keywords: list[str]
    