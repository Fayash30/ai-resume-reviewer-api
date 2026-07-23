from schemas import ResumeReviewResponse
import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def build_resume_prompt(resume: str) -> str:
    return f"""
You are an experienced technical recruiter reviewing a resume
for AI Engineer roles.

Evaluate the candidate based only on the supplied resume.

Focus on:
- AI/ML skills
- LLM/Generative AI skills
- Backend and API skills
- Projects
- Professional experience
- ATS compatibility

Do not invent experience, skills, projects, or qualifications
that are not present in the resume.

----- START RESUME -----

{resume}

----- END RESUME -----
"""

# def test_gemini():
#     response = client.models.generate_content(
#         model="gemini-3-flash-preview",
#         contents="Reply with exactly: Gemini connection successful"
#     )

#     return response.text


# print(test_gemini())

def analyze_resume(resume: str) -> ResumeReviewResponse:

    prompt = build_resume_prompt(resume)

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": ResumeReviewResponse,
        },
    )

    return ResumeReviewResponse.model_validate_json(
        response.text
    )


def get_app_name():
    return "AI Resume Reviewer API"

def get_project_metadata():
    return {
        "name": "AI Resume Reviewer",
        "version": "1.0.0",
        "author": "Mohamed Fayash"
    }