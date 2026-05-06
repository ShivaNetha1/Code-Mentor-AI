import os 
import streamlit as st
from groq import Groq
from dotenv import load_dotenv


load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

st.set_page_config(
    page_title="AI Code Assistant",
    page_icon="💻",
    layout="wide"
)

if "history" not in st.session_state:
    st.session_state.history = []

st.title("💻 AI Code Assistant")
st.write("Get help with programming code using AI, including bug detection and optimization suggestions.")

st.sidebar.header("⚙ Settings")

language = st.sidebar.selectbox(
    "Programming Language",
    ["Python","MySQL", "Java", "JavaScript", "C++", "C"]
)

mode = st.sidebar.selectbox(
    "Explanation Mode",
    ["Beginner", "Advanced"]
)

model = st.sidebar.selectbox(
    "AI Model",
    [
        "llama-3.1-8b-instant",
        "llama3-70b-8192",
        "openai/gpt-oss-20b",
        "qwen/qwen3-32b"
    ]
)

code = st.text_area(
    "📌 Write Your Code Here",
    height=200,
    placeholder="Write or paste your code here..."
)

if code:
    st.subheader("📄Your Code Preview")
    st.code(code, language=language.lower())

col1, col2 = st.columns(2)

with col1:
    explain_button = st.button("🚀 Explain Code")

with col2:
    clear_button = st.button("🗑 Clear Chat History")

if clear_button:
    st.session_state.history = []
    st.success("Chat History Cleared Successfully!")

if explain_button:

    if code.strip() == "":
        st.warning("⚠ Please enter your code.")

    else:

        with st.spinner("Generating Response.."):

            prompt = f"""
            You are an expert programming tutor and senior software engineer.

            Explain the following {language} code in {mode} mode.

            Your response should include:

            1. What the code does
            2. Step-by-step explanation
            3. Important programming concepts used
            4. Bug detection or bad practices
            5. Code optimization suggestions
            6. Time complexity if applicable
            7. Final summary

            Code:
            {code}
            """

            try:

                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=0.3
                )

                explanation = response.choices[0].message.content

                st.session_state.history.append({
                    "language": language,
                    "code": code,
                    "explanation": explanation
                })

                
                tab1, tab2 = st.tabs(
                    ["📘 Explanation", "🐞 Bug Analysis"]
                )

                with tab1:
                    st.subheader("📘 AI Explanation")

                    st.text_area(
                        "Generated Explanation",
                        explanation,
                        height=400
                    )

                with tab2:

                    bug_prompt = f"""
                    Analyze this {language} code for bugs,
                    inefficiencies, and bad coding practices.

                    Code:
                    {code}
                    """

                    bug_response = client.chat.completions.create(
                        model=model,
                        messages=[
                            {
                                "role": "user",
                                "content": bug_prompt
                            }
                        ],
                        temperature=0.2
                    )

                    bug_report = bug_response.choices[0].message.content

                    st.subheader("🐞 Bug Detection Report")

                    st.text_area(
                        "Bug Analysis",
                        bug_report,
                        height=450
                    )

            except Exception as e:
                st.error(f"Error: {e}")


if st.session_state.history:

    st.markdown("---")
    st.subheader("🕘 Previous Explanations")

    for idx, item in enumerate(reversed(st.session_state.history), start=1):

        with st.expander(f"Explanation #{idx}"):

            st.markdown(f"### 🌐 Language: {item['language']}")

            st.code(
                item["code"],
                language=item["language"].lower()
            )

            st.markdown("### 📘 Explanation")

            st.write(item["explanation"])

st.markdown("---")

st.caption(
    "🚀 Built by ShivaNetha"
)
