import json
import os

from openai import OpenAI

from .prompts import SYSTEM_PROMPT


def get_client() -> OpenAI:
    return OpenAI(
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
    )


def analyze_resume(resume_text: str, jd_text: str) -> dict:
    from .prompts import build_analysis_prompt

    client = get_client()
    user_prompt = build_analysis_prompt(resume_text, jd_text)

    response = client.chat.completions.create(
        model=os.getenv("DEEPSEEK_MODEL", "deepseek-chat"),
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.3,
        response_format={"type": "json_object"},
    )

    result = json.loads(response.choices[0].message.content)
    return result
