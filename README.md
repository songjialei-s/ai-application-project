# AI简历助手

一个帮助求职者优化简历、精准匹配岗位的智能分析工具。让AI充当"私人求职顾问"，代替人工逐一对比岗位要求和简历内容。

## 核心功能

| 功能 | 描述 | 用户价值 |
|------|------|----------|
| 简历解析 | 上传PDF简历，自动提取姓名、学校、经历、技能等结构化信息 | 省去手动录入简历信息的麻烦 |
| JD分析 | 用户手动粘贴/输入职位描述文本 | 无需爬虫，任何平台JD都能用 |
| 匹配度评估 | AI对比简历与JD，输出0-100分匹配度评分 | 直观了解自己与岗位的差距 |
| 技能标签提取 | 从JD中提取必备技能和加分技能，与简历技能对比 | 明确知道需要补什么技能 |
| 优化建议 | AI生成简历修改建议（新增项目、调整描述等） | 提供可执行的简历优化方向 |

## 技术栈

- **后端**：Python 3.11+ / FastAPI / PyMuPDF
- **前端**：Streamlit
- **AI模型**：DeepSeek Chat
- **其他**：OpenAI SDK / Pydantic v2 / python-dotenv

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置API Key

编辑 `.env` 文件，填入你的DeepSeek API Key：

```
DEEPSEEK_API_KEY=your_api_key_here
DEEPSEEK_BASE_URL=https://api.deepseek.com
DEEPSEEK_MODEL=deepseek-chat
```

### 3. 启动后端服务

```bash
uvicorn backend.main:app --reload --port 8000
```

### 4. 启动前端界面

```bash
streamlit run frontend/app.py
```

### 5. 使用

1. 打开浏览器访问 `http://localhost:8501`
2. 上传PDF格式的简历
3. 粘贴目标岗位的职位描述
4. 点击"开始分析"查看结果

## 项目结构

```
ai-application-project/
├── backend/
│   ├── __init__.py
│   ├── main.py              # FastAPI 入口，处理API请求
│   ├── pdf_parser.py        # PDF文本提取（PyMuPDF）
│   ├── llm_client.py        # DeepSeek API调用封装
│   ├── prompts.py           # Prompt模板定义
│   └── models.py            # Pydantic数据模型
├── frontend/
│   └── app.py               # Streamlit交互界面
├── .env                     # API Key配置（不提交Git）
├── .gitignore
├── requirements.txt
└── README.md
```

## API接口

| 方法 | 路径 | 功能 |
|------|------|------|
| POST | `/api/analyze` | 上传简历PDF+JD，返回分析结果 |
| GET | `/api/health` | 健康检查 |

## 分析结果示例

```json
{
  "match_score": 85,
  "matched_skills": ["Python", "FastAPI", "SQL"],
  "missing_skills": ["Docker", "Kubernetes"],
  "bonus_skills": ["Redis", "RabbitMQ"],
  "suggestions": [
    "建议在简历中增加Docker容器化部署经验",
    "可以补充Kubernetes集群管理相关项目",
    "简历中可以增加更多量化的工作成果"
  ],
  "resume_summary": "3年Python后端开发经验，熟悉Web框架和数据库..."
}
```

## 版本规划

| 版本 | 功能范围 | 状态 |
|------|----------|------|
| V1.0 MVP | PDF上传 + JD粘贴 + 匹配度评分 + 技能标签 + 优化建议 | 当前版本 |
| V1.1 | 历史记录保存（SQLite/JSON） | 规划中 |
| V1.2 | 支持Word格式简历 | 规划中 |
| V2.0 | 爬虫自动抓取招聘网站JD | 规划中 |

## 许可证

MIT License
