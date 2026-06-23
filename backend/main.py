import os

from dotenv import load_dotenv
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from .llm_client import analyze_resume
from .models import AnalyzeRequest, AnalyzeResponse
from .pdf_parser import extract_text_from_pdf

load_dotenv()

app = FastAPI(title="AI简历助手", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health_check():
    return {"status": "ok"}


@app.post("/api/analyze", response_model=AnalyzeResponse)
async def analyze(file: UploadFile = File(...), jd_text: str = ""):
    pdf_bytes = await file.read()
    resume_text = extract_text_from_pdf(pdf_bytes)

    if not resume_text:
        return AnalyzeResponse(
            match_score=0,
            matched_skills=[],
            missing_skills=[],
            bonus_skills=[],
            suggestions=["无法从PDF中提取文本，请确保PDF包含可复制的文字内容"],
            resume_summary="PDF解析失败",
        )

    result = analyze_resume(resume_text, jd_text)
    return AnalyzeResponse(**result)
