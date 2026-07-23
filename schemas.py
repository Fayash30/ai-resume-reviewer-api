from pydantic import BaseModel, Field


class ResumeRequest(BaseModel):
    resume: str = Field(
        min_length=50,
        description="Extracted resume text to analyze"
    )
 
class ResumeReviewResponse(BaseModel):
    score: int
    strengths: list[str]
    weaknesses: list[str]
    summary: str
    recommendations: list[str]
    keywords: list[str]
    