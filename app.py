from openai import OpenAI

client = OpenAI(api_key="your_api_key")

prompt = "分析新能源汽车充电桩用户需求"

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"user","content":prompt}
    ]
)

print(response.choices[0].message.content)