from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    jd_text: str


class AnalyzeResponse(BaseModel):
    match_score: int
    matched_skills: list[str]
    missing_skills: list[str]
    bonus_skills: list[str]
    suggestions: list[str]
    resume_summary: str
