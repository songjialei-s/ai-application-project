import streamlit as st
import requests

API_URL = "http://localhost:8000/api"

st.set_page_config(page_title="AI简历助手", page_icon="📄", layout="wide")

st.title("AI简历助手")
st.markdown("上传简历PDF，粘贴岗位描述，AI帮你分析匹配度并提供优化建议")

col1, col2 = st.columns(2)

with col1:
    st.subheader("上传简历")
    uploaded_file = st.file_uploader("选择PDF文件", type=["pdf"])

with col2:
    st.subheader("岗位描述")
    jd_text = st.text_area("粘贴岗位描述(JD)", height=300)

if st.button("开始分析", type="primary", use_container_width=True):
    if not uploaded_file:
        st.error("请先上传简历PDF文件")
    elif not jd_text.strip():
        st.error("请输入岗位描述")
    else:
        with st.spinner("AI正在分析中，请稍候..."):
            try:
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
                data = {"jd_text": jd_text}
                response = requests.post(f"{API_URL}/analyze", files=files, data=data)

                if response.status_code == 200:
                    result = response.json()

                    st.divider()
                    st.subheader("分析结果")

                    score = result["match_score"]
                    if score >= 70:
                        st.success(f"匹配度评分：{score}/100")
                    elif score >= 50:
                        st.warning(f"匹配度评分：{score}/100")
                    else:
                        st.error(f"匹配度评分：{score}/100")

                    col_a, col_b = st.columns(2)

                    with col_a:
                        st.markdown("**匹配的技能**")
                        for skill in result["matched_skills"]:
                            st.markdown(f"- {skill}")

                        st.markdown("**加分技能**")
                        for skill in result["bonus_skills"]:
                            st.markdown(f"- {skill}")

                    with col_b:
                        st.markdown("**缺失的技能**")
                        for skill in result["missing_skills"]:
                            st.markdown(f"- {skill}")

                    st.divider()
                    st.subheader("优化建议")
                    for i, suggestion in enumerate(result["suggestions"], 1):
                        st.markdown(f"{i}. {suggestion}")

                    st.divider()
                    st.subheader("简历摘要")
                    st.text(result["resume_summary"])

                else:
                    st.error(f"分析失败：{response.text}")

            except requests.exceptions.ConnectionError:
                st.error("无法连接到后端服务，请确保FastAPI服务已启动")
            except Exception as e:
                st.error(f"发生错误：{str(e)}")
